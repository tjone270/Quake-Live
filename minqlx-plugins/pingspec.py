# Created by Thomas Jones on 17/12/2015 - thomas@tomtecsolutions.com
# pingspec.py, a plugin for minqlx to spec players who have network latency over a certain amount.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for line one, two, three and four. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx

class pingspec(minqlx.Plugin):
    def __init__(self):
        self.add_hook("frame", self.process_frame, priority=minqlx.PRI_LOWEST)
        self.add_command("tomtec_versions", self.cmd_showversion)
        
        self.seconds_between_checks = 15
        self.max_ping = 125

        self.plugin_version = "1.1"
        
        # Don't touch this:
        self.frame_counter = 0


    def process_frame(self):
        self.frame_counter += 1
        if self.frame_counter == (self.seconds_between_checks * int(minqlx.get_cvar("sv_fps"))):
            self.frame_counter = 0
            self.check_ping()

    def check_ping(self):
        for player in self.players():
            if player.ping > self.max_ping:
                if self.game.state == "warmup":
                    player.tell("^1Your ping is over the maximum ping tolerated here ({}). You will be put to spec if it remains above the threshold.".format(self.max_ping))
                else:
                    if player.team != "spectator":
                        player.put("spectator")
                        self.msg("{} has been put in spec automatically for having a ping over {}.".format(player.clean_name, self.max_ping))
                        player.tell("^1Your ping is over {}, the threshold.^7 You have been put in spec.".format(self.max_ping))

    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4pingspec.py^7 - version {}, created by Thomas Jones on 17/12/2015.".format(self.plugin_version))
