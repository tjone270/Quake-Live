# Created by Thomas Jones on 19/12/2015 - thomas@tomtecsolutions.com
# voteshow.py, a plugin for minqlx to show who votes yes or no in-game.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for line one, two, three and four. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx

class voteshow(minqlx.Plugin):
    def __init__(self):
        self.add_hook("vote", self.process_vote, priority=minqlx.PRI_LOWEST)
        self.add_command("tomtec_versions", self.cmd_showversion)
        
        self.plugin_version = "1.0"


    def process_vote(self, player, yes):
        if yes:
            word = "^2yes"
        else:
            word = "^1no"
            
        self.msg("{}^7 voted {}^7.".format(player.name, word))
    
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4voteshow.py^7 - version {}, created by Thomas Jones on 19/12/2015.".format(self.plugin_version))
