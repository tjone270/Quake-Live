# Created by Thomas Jones on 22/12/2015 - thomas@tomtecsolutions.com
# locations.py, a plugin for minqlx to approximately geo-locate players.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

# This plugin uses the free Geo-IP API from http://freegeoip.net.

"""
The following cvars are used on this plugin:
    qlx_locationCommandPermissionRequired: Required permission level to run the !loc and !location commands. Default: 1
"""

import minqlx
import requests
import json
import threading

class locations(minqlx.Plugin):
    def __init__(self):
        self.set_cvar_once("qlx_locationCommandPermissionRequired", "1")
        
        self.add_command(("loc", "location"), self.cmd_location, (self.get_cvar("qlx_locationCommandPermissionRequired", int)), usage="<id>")
        self.add_command("tomtec_versions", self.cmd_showversion)
        
        self.plugin_version = "1.1"

    @minqlx.thread
    def cmd_location(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.RET_USAGE
        
        try:
            player_ip = self.player(int(msg[1])).ip
            player_name = self.player(int(msg[1])).name
        except:
            channel.reply("^1Invalid Client ID.^7 Enter a valid client ID to see their approximate location.")
            return
    
        ipData = requests.get('http://freegeoip.net/json/{}'.format(player_ip), stream=True)
        ipData = str(ipData.text)
        ipDataParsed = json.loads(ipData)

        channel.reply("{}^7's approximate location details:\n    Country Code: {}\n    Country Name: {}\n    Region Code: {}\n    Region Name: {}\n    City: {}\n    Post Code: {}\n    Time Zone: {}".format(player_name, ipDataParsed['country_code'], ipDataParsed['country_name'], ipDataParsed['region_code'], ipDataParsed['region_name'], ipDataParsed['city'], ipDataParsed['zip_code'], ipDataParsed['time_zone']))

        return minqlx.RET_STOP_ALL
    
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4locations.py^7 - version {}, created by Thomas Jones on 22/01/2016.".format(self.plugin_version))
