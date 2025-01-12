# 13/01/2025 - tjone270
# a minqlx plugin to list all players with a permission level greater than 0.

import minqlx


class permissionlist(minqlx.Plugin):
    def __init__(self):
        self.add_command("permissionlist", self.cmd_permissionlist, 5, usage="<level>")

    @minqlx.thread
    def cmd_permissionlist(self, player, msg, channel):
        """Lists all players with a permission level greater than 0."""

        players_permissions = {}
        for key in self.db.keys("minqlx:players:*:permission"):
            steam_id = int(key.split(":")[2])
            permission = int(self.db.get(key))

            if permission > 0:
                players_permissions[steam_id] = permission

        players_permissions = dict(sorted(players_permissions.items(), key=lambda x: x[1]))

        channel.reply("^7Permissions list:")
        for steam_id, permission in players_permissions.items():
            channel.reply(" {}^7: ^2{}^7".format(steam_id, permission))
