# Created by Thomas Jones on 26/07/2017 - thomas@tomtecsolutions.com
# sv_fps.py, a plugin for minqlx to modify the previously unmodifiable sv_fps cvar.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D
import minqlx

STD_SVFPS = 40
class sv_fps(minqlx.Plugin):
    def __init__(self):
        self.add_command(("sv_fps", "svfps"), self.cmd_svfps, 5, usage="<integer>")
        self.add_command("tomtec_versions", self.cmd_showversion)
        self.set_cvar_once("qlx_svfps", str(STD_SVFPS))
        self.plugin_version = "1.2"
        self.set_initial_fps(self.get_cvar("qlx_svfps", int))

        
    def cmd_svfps(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.RET_USAGE

        try:
            sv_fps = int(msg[1])
        except ValueError:
            channel.reply("You must specify a positive integer greater than or equal to {}.".format(STD_SVFPS))
            return minqlx.RET_STOP

        if (self.check_value(sv_fps, channel)):
            minqlx.set_cvar("sv_fps", str(sv_fps), -1)
            channel.reply("sv_fps is now set to {}.".format(sv_fps))

    @minqlx.delay(5)
    def set_initial_fps(self, cvarval):
        if (cvarval != STD_SVFPS):
            if (self.check_value(cvarval, minqlx.CHAT_CHANNEL)):
                minqlx.set_cvar("sv_fps", str(cvarval), -1)
            else:
                self.msg("Will not set sv_fps to value of qlx_svfps as the latter contains an incompatible value.")
        else:
            pass 
        
    def check_value(self, sv_fps, channel):
        ret = True
        if (sv_fps < 0):
            channel.reply("The integer specified must be positive.")
            ret = False
        if (sv_fps < STD_SVFPS):
            channel.reply("The integer specified must not be less than the preset sv_fps value ({})".format(STD_SVFPS))
            ret = False
        if ((sv_fps % STD_SVFPS) != 0):
            channel.reply("The integer specified must be divisible by {}. ({}, {}, {}, {} etc)".format(STD_SVFPS,
                                                                                                       STD_SVFPS*2,
                                                                                                       STD_SVFPS*3,
                                                                                                       STD_SVFPS*4,
                                                                                                       STD_SVFPS*5))
            ret = False
        return ret

    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4sv_fps.py^7 - version {}, created by Thomas Jones on 26/07/2017.".format(self.plugin_version))
