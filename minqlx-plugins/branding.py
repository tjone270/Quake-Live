# Created by Thomas Jones on 06/11/15 - thomas@tomtecsolutions.com
# branding.py, a plugin for minqlx to brand your server.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

"""
Branding.py is a minqlx plugin that permits you to personalise your server with your own information.
Simply put the plugin in the 'minqlx-plugins' folder, !load the plugin, and set these cvars:

    qlx_serverBrandName                  - Where the map name usually appears, the text set in this cvar will appear instead.
    qlx_serverBrandTopField              - Where the map author credit (line 1) appears, the text set in this cvar will appear after the credit.
    qlx_serverBrandBottomField           - Where the map author credit (line 2) appears, the text set in this cvar will appear after the credit.

    qlx_connectMessage                   - When the player is at the awaiting challenge screen when they first connect to the server, text will appear here.
    qlx_loadedMessage                    - When the player gets to the menu after connecting, and clicks Join or Spectate, they'll get centre print from this cvar.
    qlx_countdownMessage                 - When the countdown begins, this text will appear mid-screen. (like the qlx_loadedMessage does)
    qlx_endOfGameMessage                 - When the game finishes, it'll put the text in this cvar in the text box on the left.
    
    qlx_brandingPrependMapName           - This cvar will put the map name before your qlx_serverBrandName.                     Default: 0
    qlx_brandingAppendGameType           - Will add the game type after your qlx_serverBrandName.                               Default: 0
    qlx_rainbowBrandName                 - Make the entire map name (qlx_serverBrandName) appear in rainbow colouring.          Default: 0
    
Once set, change maps, and you'll see the map loading screen is changed.
"""

import minqlx

class branding(minqlx.Plugin):
    def __init__(self):
        self.add_hook("new_game", self.brand_map)
        self.add_hook("player_connect", self.player_connect)
        self.add_hook("player_loaded", self.player_loaded)
        self.add_hook("game_countdown", self.game_countdown)
        self.add_hook("game_end", self.game_end)
        
        self.add_command("tomtec_versions", self.cmd_showversion)

        self.set_cvar_once("qlx_brandingPrependMapName", "0")
        self.set_cvar_once("qlx_brandingAppendGameType", "0")
        self.set_cvar_once("qlx_rainbowBrandName", "0")
        
        self.plugin_version = "2.1"

        self.playerConnectedYetList = []
        
    def brand_map(self):
        if self.get_cvar("qlx_serverBrandName") == None:
            self.set_cvar("qlx_serverBrandName", self.game.map_title)
            
        if self.get_cvar("qlx_brandingPrependMapName", bool):
            topBranding = self.game.map_title + " " + self.get_cvar("qlx_serverBrandName")
        else:
            topBranding = self.get_cvar("qlx_serverBrandName")

        if self.get_cvar("qlx_brandingAppendGameType", bool):
            minqlx.set_configstring(3, topBranding + " " + self.game.type)
        else:
            minqlx.set_configstring(3, topBranding)

        if self.get_cvar("qlx_serverBrandTopField") != None:
            cs = self.game.map_subtitle1
            if cs:
                cs += " - "
            minqlx.set_configstring(678, cs + (self.get_cvar("qlx_serverBrandTopField")))

        if self.get_cvar("qlx_serverBrandBottomField") != None:
            cs = self.game.map_subtitle2
            if cs:
                cs += " - "
            minqlx.set_configstring(679, cs + (self.get_cvar("qlx_serverBrandBottomField")))

        if self.get_cvar("qlx_rainbowBrandName", bool):
            # Thanks Mino for this bit!
            def rotating_colors():
                i = 0
                while True:
                    res = (i % 7) + 1
                    i += 1
                    yield res

            map_name = self.clean_text(minqlx.get_configstring(3))
            r = rotating_colors()
            res = ""
            for i in range(len(map_name)):
                res += "^{}{}".format(next(r), map_name[i])

            minqlx.set_configstring(3, res)

    def player_connect(self, player):
        if self.get_cvar("qlx_connectMessage") != None:
            if player not in self.playerConnectedYetList:
                self.playerConnectedYetList.append(player)
                return "{}\n^7This server is running ^4branding.py^7. ^2http://github.com/tjone270/Quake-Live^7.\n".format(self.get_cvar("qlx_connectMessage"))
        
    def player_loaded(self, player):
        if self.get_cvar("qlx_loadedMessage") != None:
            self.center_print(self.get_cvar("qlx_loadedMessage"), player.id)

        try:
            self.playerConnectedYetList.remove(player)
        except:
            return

    def game_countdown(self):
        if self.get_cvar("qlx_countdownMessage") != None:
            self.center_print(self.get_cvar("qlx_countdownMessage"))

    def game_end(self, data):
        if self.get_cvar("qlx_endOfGameMessage") != None:
            self.msg(self.get_cvar("qlx_endOfGameMessage"))

            
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4branding.py^7 - version {}, created by Thomas Jones on 06/11/2015.".format(self.plugin_version))
