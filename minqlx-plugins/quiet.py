# Created by Thomas Jones on 10/01/2016 - thomas@tomtecsolutions.com
# quiet.py - a minqlx plugin to disable chat during a match. Designed for PerpetualWar on QuakeNet IRC (#qldedsrv)
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

"""
This plugin will prevent anyone who is not QLDS Admin/Mod or at least minqlx Permlevel 4 from using /tell, /say_team and /say during a match.
Talking is permitted during warmup by default, setting the following cvar to 0 will disable that functionality as well: qlx_permitChatDuringWarmup
"""

import minqlx

class quiet(minqlx.Plugin):
    def __init__(self):
        self.add_hook("client_command", self.handle_client_command)
        self.add_hook("game_countdown", self.game_countdown)
        
        self.add_command("tomtec_versions", self.cmd_showversion)

        self.set_cvar_once("qlx_permitChatDuringWarmup", "1")
        
        self.plugin_version = "1.2"


    def handle_client_command(self, player, cmd):
        if self.game.state != "warmup":
            if (cmd.lower().startswith("say ") or cmd.lower().startswith("say_team ") or cmd.lower().startswith("tell ")):
                ident = player.steam_id
                if not (player.privileges in ["admin", "mod"] or self.db.has_permission(ident, 4)):
                    player.tell("Chat is disabled during the match.")
                    return minqlx.RET_STOP_ALL
        else:
            if not (self.get_cvar("qlx_permitChatDuringWarmup", bool)):
                if (cmd.lower().startswith("say ") or cmd.lower().startswith("say_team ") or cmd.lower().startswith("tell ")):
                    ident = player.steam_id
                    if not (player.privileges in ["admin", "mod"] or self.db.has_permission(ident, 4)):
                        player.tell("Chat is disabled during the match.")
                        return minqlx.RET_STOP_ALL

    def game_countdown(self):
        self.msg("Chat is now disabled during the match.")
                
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4quiet.py^7 - version {}, created by Thomas Jones on 10/01/2016.".format(self.plugin_version))
