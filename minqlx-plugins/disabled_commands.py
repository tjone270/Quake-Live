# Created by Thomas Jones on 11/04/16 - thomas@tomtecsolutions.com
# disabled_commands.py, a plugin for minqlx to display a message when a disabled command is run.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

DISABLED_COMMANDS = () # example: ("elo", "teens", "do", "balance")


import minqlx
class disabled_commands(minqlx.Plugin):
    def __init__(self):
        self.add_command(DISABLED_COMMANDS, self.cmd_display_message, priority=minqlx.PRI_HIGHEST)
        self.add_command("tomtec_versions", self.cmd_showversion)

        self.plugin_version = "1.0"

    def cmd_display_message(self, player, msg, channel):
        channel.reply("The ^4{}^7 command is disabled on this server.".format(msg[0]))
        return minqlx.RET_STOP_ALL
    
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4disabled_commands.py^7 - version {}, created by Thomas Jones on 11/04/2016.".format(self.plugin_version))
