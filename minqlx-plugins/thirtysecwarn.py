# Created by Thomas Jones on 01/09/2016 - thomas@tomtecsolutions.com
# thirtysecwarn.py - a minqlx plugin to play unused VO when a CA game is nearing the round time limit.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx, time
class thirtysecwarn(minqlx.Plugin):
    def __init__(self):
        self.add_hook("round_start", self.handle_round_start)
        self.add_hook("game_end", self.handle_game_end)
        self.add_command("tomtec_versions", self.cmd_showversion)

        self.plugin_version = 1.1
        self.roundnumber = 0


    @minqlx.thread
    def handle_round_start(self, *args, **kwargs):
        self.roundnumber += 1
        if self.game.type_short == "ca":
            currentroundnumber = self.roundnumber
            roundtimelimit = self.get_cvar("roundtimelimit", int)
            minusthirtyseconds = (roundtimelimit - 30)
            time.sleep(minusthirtyseconds)
            if (self.game.state == "in_progress") and (currentroundnumber == self.roundnumber):
                self.play_sound("sound/vo/30_second_warning.ogg")
                
        return minqlx.RET_NONE

    def handle_game_end(self, *args, **kwargs):
        self.roundnumber = 0
        
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4thirtysecwarn.py^7 - version {}, created by Thomas Jones on 01/09/16.".format(self.plugin_version))
