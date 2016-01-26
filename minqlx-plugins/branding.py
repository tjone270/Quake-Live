# Created by Thomas Jones on 06/11/15 - thomas@tomtecsolutions.com
# branding.py, a plugin for minqlx to brand your server.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

"""
Branding.py is a minqlx plugin that permits you to modify your map loading screen with your own information.
Simply put the plugin in the 'minqlx-plugins' folder, !load the plugin, and set these cvars:

    qlx_serverBrandName
    qlx_serverBrandTopField
    qlx_serverBrandBottomField

Once set, change maps, and you'll see the map loading screen is changed.
"""

import minqlx

class branding(minqlx.Plugin):
    def __init__(self):
        self.add_hook("new_game", self.brand_map)
        self.add_command("tomtec_versions", self.cmd_showversion)
        self.set_cvar_once("qlx_serverBrandName", "Branding isn't set up!")
        self.set_cvar_once("qlx_serverBrandTopField", "Set these cvars: 'qlx_serverBrandName', 'qlx_serverBrandTopField', 'qlx_serverBrandBottomField'.")
        self.set_cvar_once("qlx_serverBrandBottomField", "Tip: ^1C^2o^3l^4o^5u^6r ^1v^2a^3l^4u^5e^6s ^1a^2r^3e ^1s^2u^3p^4p^5o^6r^1t^2e^3d^4.")

        self.plugin_version = "1.4"
        
    def brand_map(self):
        minqlx.set_configstring(3, (self.get_cvar("qlx_serverBrandName")))
        cs = self.game.map_subtitle1
        if cs:
            cs += " - "
        minqlx.set_configstring(678, cs + (self.get_cvar("qlx_serverBrandTopField")))
        cs = self.game.map_subtitle2
        if cs:
            cs += " - "
        minqlx.set_configstring(679, cs + (self.get_cvar("qlx_serverBrandBottomField")))

    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4branding.py^7 - version {}, created by Thomas Jones on 06/11/2015.".format(self.plugin_version))
