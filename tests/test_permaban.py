"""Synthetic regression tests; do not import minqlx or connect to Redis."""

import ast
import pathlib
import types
import unittest


def isolated_plugin_class():
    path = pathlib.Path(__file__).resolve().parents[1] / "minqlx-plugins/permaban.py"
    tree = ast.parse(path.read_bytes(), filename=str(path))
    plugin = next(node for node in tree.body if isinstance(node, ast.ClassDef))
    methods = [
        node
        for node in plugin.body
        if isinstance(node, ast.FunctionDef)
        and node.name in {"is_banned", "handle_player_connect"}
    ]
    if len(methods) != 2:
        raise AssertionError("Expected both ban-check methods")
    isolated = ast.Module(
        body=[
            ast.ClassDef(
                name="BanLogic", bases=[], keywords=[], body=methods, decorator_list=[]
            )
        ],
        type_ignores=[],
    )
    namespace = {}
    exec(compile(ast.fix_missing_locations(isolated), str(path), "exec"), namespace)
    return namespace["BanLogic"]


BanLogic = isolated_plugin_class()


def ban_key(account):
    return f"minqlx:players:{account}:permabanned"


class FakeRedis:
    def __init__(self):
        self.sets = {}
        self.values = {}
        self.calls = []

    def get(self, key):
        self.calls.append(("get", key))
        return self.values.get(key)

    def smembers(self, key):
        self.calls.append(("smembers", key))
        return set(self.sets.get(key, set()))

    def sunion(self, keys):
        self.calls.append(("sunion", list(keys)))
        return set().union(*(self.sets.get(key, set()) for key in keys))

    def mget(self, keys):
        self.calls.append(("mget", list(keys)))
        return [self.values.get(key) for key in keys]

    def set(self, key, value):
        self.calls.append(("set", key, value))
        self.values[key] = value


class PermabanTests(unittest.TestCase):
    def setUp(self):
        self.db = FakeRedis()
        self.plugin = BanLogic()
        self.plugin.db = self.db
        self.player = types.SimpleNamespace(steam_id=101, ip="192.0.2.1")

    def associate(self, address, *accounts):
        self.db.sets[f"minqlx:ips:{address}"] = {str(account) for account in accounts}

    def history(self, *addresses):
        self.db.sets["minqlx:players:101:ips"] = set(addresses)

    def test_own_ban_returns_before_association_queries(self):
        self.db.values[ban_key(101)] = "1"
        self.assertEqual(self.plugin.is_banned(self.player), 101)
        self.assertEqual(self.db.calls, [("get", ban_key(101))])

    def test_no_history_and_no_associations_allow_connection(self):
        self.assertIs(self.plugin.is_banned(self.player), False)
        self.assertEqual([c[0] for c in self.db.calls], ["get", "smembers", "sunion"])

    def test_current_address_is_checked_without_history(self):
        self.associate(self.player.ip, 202)
        self.db.values[ban_key(202)] = "1"
        self.assertEqual(self.plugin.is_banned(self.player), "202")

    def test_historical_address_is_still_checked(self):
        self.history("192.0.2.2")
        self.associate("192.0.2.2", 202)
        self.db.values[ban_key(202)] = "1"
        self.assertEqual(self.plugin.is_banned(self.player), "202")

    def test_repeated_accounts_and_current_address_are_deduplicated(self):
        addresses = [f"2001:db8:{index:x}::1" for index in range(1028)]
        self.player.ip = addresses[0]
        self.history(*addresses)
        for address in addresses:
            self.associate(address, 101, 202)
        self.assertIs(self.plugin.is_banned(self.player), False)
        self.assertEqual(len(self.db.calls), 4)
        self.assertEqual(len(self.db.calls[2][1]), 1028)
        self.assertEqual(set(self.db.calls[3][1]), {ban_key(101), ban_key(202)})

    def test_unbanned_and_missing_flags_do_not_ban(self):
        self.associate(self.player.ip, 202, 303)
        self.db.values[ban_key(202)] = "0"
        self.assertIs(self.plugin.is_banned(self.player), False)

    def test_any_banned_associated_account_blocks(self):
        self.associate(self.player.ip, 202, 303, 404)
        self.db.values[ban_key(303)] = "1"
        self.assertEqual(self.plugin.is_banned(self.player), "303")

    def test_ban_changes_are_not_cached(self):
        self.associate(self.player.ip, 202)
        self.assertIs(self.plugin.is_banned(self.player), False)
        self.db.values[ban_key(202)] = "1"
        self.assertEqual(self.plugin.is_banned(self.player), "202")
        del self.db.values[ban_key(202)]
        self.assertIs(self.plugin.is_banned(self.player), False)

    def test_own_ban_keeps_original_rejection(self):
        self.db.values[ban_key(101)] = "1"
        self.assertEqual(
            self.plugin.handle_player_connect(self.player),
            "Your account is permabanned.\n",
        )
        self.assertFalse(any(c[0] == "set" for c in self.db.calls))

    def test_associated_ban_keeps_rejection_and_propagation(self):
        self.associate(self.player.ip, 202)
        self.db.values[ban_key(202)] = "1"
        self.assertEqual(
            self.plugin.handle_player_connect(self.player),
            "Your associated accounts are permabanned.\n",
        )
        self.assertEqual(self.db.values[ban_key(101)], "1")
        self.assertEqual(
            [c for c in self.db.calls if c[0] == "set"],
            [("set", ban_key(202), "1"), ("set", ban_key(101), "1")],
        )

    def test_successful_connection_does_not_write(self):
        self.associate(self.player.ip, 202)
        self.assertIsNone(self.plugin.handle_player_connect(self.player))
        self.assertFalse(any(c[0] == "set" for c in self.db.calls))

    def test_database_error_does_not_become_success(self):
        def unavailable(_keys):
            raise ConnectionError("synthetic database unavailable")

        self.db.sunion = unavailable
        with self.assertRaises(ConnectionError):
            self.plugin.handle_player_connect(self.player)


if __name__ == "__main__":
    unittest.main()
