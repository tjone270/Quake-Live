# Created by Thomas Jones on 14/12/2015 - thomas@tomtecsolutions.com
# aliases.py, a plugin for minqlx to show aliases from the redis database.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx
import minqlx.database

class aliases(minqlx.Plugin):
    database = minqlx.database.Redis
    
    def __init__(self):
        self.add_command("alias", self.cmd_alias, usage="<id>")
        self.add_command("clearaliases", self.cmd_clearaliases, 5)
        self.add_command("tomtec_versions", self.cmd_showversion)

        self.plugin_version = "1.6"

    def cmd_alias(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.RET_USAGE
        
        try:
            steam_id = self.player(int(msg[1])).steam_id
            player_name = self.player(int(msg[1])).name
        except:
            channel.reply("^1Invalid Client ID.^7 Enter a valid client ID to see a list of names they've used on this server.")
            return
        
        key = "minqlx:players:{}".format(steam_id)
        out = list(self.db.lrange(key, 0, -1))
        channel.reply("{}^7 has played on this server under the following names:".format(player_name))
        channel.reply(" ^4*^7  {}".format("   \n ^4*^7  ".join(out)))

    def cmd_clearaliases(self, player, msg, channel):
        # this function came from namesfix.py by Mino
        players = self.db.smembers("minqlx:players")
        for p in players:
            del self.db["minqlx:players:{}".format(p)]
        channel.reply("All aliases for all players ({} players in total) were cleared.".format(len(players)))

    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4aliases.py^7 - version {}, created by Thomas Jones on 14/12/2015.".format(self.plugin_version))
