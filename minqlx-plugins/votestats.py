# Created by Thomas Jones on 01/01/2016 - thomas@tomtecsolutions.com
# votestats.py - a minqlx plugin to show who votes yes or no in-game/vote results.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for line one, two, three and four. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx

class votestats(minqlx.Plugin):
    def __init__(self):
        self.add_hook("vote", self.process_vote, priority=minqlx.PRI_LOWEST)
        self.add_hook("vote_ended", self.handle_vote_ended, priority=minqlx.PRI_LOWEST)
        
        self.add_command("tomtec_versions", self.cmd_showversion)
        
        self.plugin_version = "1.2"


    def process_vote(self, player, yes):
        if yes:
            word = "^2yes"
        else:
            word = "^1no"
            
        self.msg("{}^7 voted {}^7.".format(player.name, word))

    def handle_vote_ended(self, votes, vote, args, passed):
        self.msg("Vote results: ^2{}^7 - ^1{}^7.".format(*votes))
        
        if passed:
            if vote.lower() == "map":
                if len(args) > 1:
                    changingToMapAndMode = args.lower().split()
                    theMsg = "The map is changing to ^4{}^7, with new game type ^4{}^7.".format(changingToMapAndMode[0], changingToMapAndMode[1])
                else:
                    theMsg = "The map is changing to ^4{}^7, with same game type ({}).".format(args.lower(), self.game.factory)

                self.msg(theMsg)
    
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4votestats.py^7 - version {}, created by Thomas Jones on 01/01/2016.".format(self.plugin_version))
