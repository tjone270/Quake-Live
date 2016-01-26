# Created by Thomas Jones on 27/01/2016 - thomas@tomtecsolutions.com
# changemap.py, a plugin for minqlx to change the map when no-one's connected.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

"""
    This plugin will change the map to the mapname set in the following cvars:
        qlx_defaultMapToChangeTo              - Default: campgrounds
        qlx_defaultMapFactoryToChangeTo       - Default: ffa
"""

import minqlx

class changemap(minqlx.Plugin):
    def __init__(self):
        self.add_hook("player_disconnect", self.player_disconnect)

        self.add_command("tomtec_versions", self.cmd_showversion)

        self.set_cvar_once("qlx_defaultMapToChangeTo", "campgrounds")
        self.set_cvar_once("qlx_defaultMapFactoryToChangeTo", "ffa")
        
        self.plugin_version = "1.0"

    def player_disconnect(self, player, reason):
        if len(self.players()) <= 1:
            self.change_map(self.get_cvar("qlx_defaultMapToChangeTo"), self.get_cvar("qlx_defaultMapFactoryToChangeTo"))
        
        
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4changemap.py^7 - version {}, created by Thomas Jones on 27/01/2016.".format(self.plugin_version))
