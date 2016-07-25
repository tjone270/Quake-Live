# Created by Thomas Jones on 21/01/2016 - thomas@tomtecsolutions.com
# ips.py, a plugin for minqlx to show a list of IPs that a player has used to connect to the server. Reads from the Redis database.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx
import minqlx.database

class ips(minqlx.Plugin):
    database = minqlx.database.Redis
    
    def __init__(self):
        self.add_command("ip", self.cmd_ip, 2, usage="<id>")
        self.add_command("tomtec_versions", self.cmd_showversion)

        self.plugin_version = "1.0"

    def cmd_ip(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.RET_USAGE
        
        try:
            ident = int(msg[1])
            target_player = None
            if 0 <= ident < 64:
                steam_id = self.player(int(msg[1])).steam_id
                player_name = self.player(int(msg[1])).name
            else:
                player_name = ident
                steam_id = ident
        except ValueError:
            channel.reply("Invalid ID. Use either a client ID or a SteamID64.")
            return
        except minqlx.NonexistentPlayerError:
            channel.reply("Invalid client ID. Use either a client ID or a SteamID64.")
            return
        
        key = "minqlx:players:{}:ips".format(steam_id)
        out = list(self.db.smembers(key))
        channel.reply("{}^7 has played on this server using the following IP addresses:".format(player_name))
        channel.reply(" ^4*^7  {}".format("   \n ^4*^7  ".join(out)))
        
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4ips.py^7 - version {}, created by Thomas Jones on 21/01/2016.".format(self.plugin_version))
