# Created by Thomas Jones on 16/05/2016 - thomas@tomtecsolutions.com
# autorestart.py, a plugin for minqlx to automatically restart a server at a certain time if no-one's connected.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

"""
    You'll need to install the schedule library. Enter the following command at your terminal to install:
        sudo python3.5 -m pip install schedule

    Times are specified in 24-hour time syntax, 13:00 for 1:00pm, 23:00 for 11:00pm, 02:00 for 2:00am etc.
"""

import minqlx, time

try:
    import schedule
except ImportError:
    minqlx.CHAT_CHANNEL.reply("^1Error:^7 The ^4schedule^7 python library isn't installed.")
    minqlx.CHAT_CHANNEL.reply("^1Error:^7 Run the following on your server to install: ^2sudo python3.5 -m pip install schedule^7")
    raise ImportError

class autorestart(minqlx.Plugin):
    def __init__(self):
        self.set_cvar_once("qlx_autoRestartTime", "00:00") # 12:00am

        self.add_command("tomtec_versions", self.cmd_showversion)

        self.add_hook("player_disconnect", self.handle_player_disconnect)

        self.plugin_version = "1.1"
        self.restart = False
        
        self.initialise()
        
        
    def initialise(self):
        schedule.every().day.at(self.get_cvar("qlx_autoRestartTime")).do(self.server_shutdown)

        @minqlx.thread
        def loop():
            while True:
                schedule.run_pending()
                time.sleep(1)
        loop()

    def handle_player_disconnect(self, *args, **kwargs):
        if len(self.players()) <= 1 and self.restart:
            minqlx.console_command("killserver")
            
    def server_shutdown(self):
        self.restart = True
        if len(self.players()) < 1:
            minqlx.console_command("killserver")

    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4autorestart.py^7 - version {}, created by Thomas Jones on 16/05/2016.".format(self.plugin_version))
