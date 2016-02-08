# Created by Thomas Jones on 08/02/16 - thomas@tomtecsolutions.com
# clanspinner.py, a plugin for minqlx to animate the clan tag.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx
import time

class clanspinner(minqlx.Plugin):
    def __init__(self):
        self.add_hook("player_loaded", self.handle_player_loaded)
        self.add_hook("player_disconnect", self.handle_player_disconnect)
        self.add_hook("unload", self.handle_plugin_unload)
        self.add_hook("console_print", self.handle_console_print)
        
        self.add_command("tomtec_versions", self.cmd_showversion)
        self.add_command("clanspinner", self.cmd_clanspinner, 5, usage="debug commands: [break, pause, continue, initialise]")
        
        self.clanMembers = []
        self.clanTag = "^0kolo^6."
        self.clanAnimation = ["^0k^6.^0olo", "^0ko^6.^0lo", "^0kol^6.^0o", "^0kolo^6.", "^0kol^6.^0o", "^0ko^6.^0lo", "^0k^6.^0olo", "^6.^0kolo"]
        self.clanAnimationDelay = 0.5
        
        self.keep_going = True
        self.pauseAnimation = True
        self.initialise()

        self.plugin_version = "0.9"

    def cmd_clanspinner(self, player, msg, channel):
        if len(msg) <= 1:
            return minqlx.RET_USAGE
        
        if msg[1].lower() == "break":
            self.keep_going = False

        if msg[1].lower() == "pause":
            self.pauseAnimation = True

        if msg[1].lower() == "continue":
            self.keep_going = True
            self.pauseAnimation = False
            
        if msg[1].lower() == "initialise":
            self.initialise()

    def handle_console_print(self, text):
        # Detect the map is changing and pause the for-loop, and clear the clanMembers list so handle_player_loaded can repopulate it.
        if "==== ShutdownGame ====" in text:
            self.pauseAnimation = True
            self.clanMembers = []
        
    def handle_plugin_unload(self, plugin):
        # Stop the while true loop
        if plugin == "clanspinner":
            self.keep_going = False

        # Restore original clan tags
        for p in self.clanMembers:
            p.clan = self.clanTag
            
    @minqlx.next_frame # Runs on the next frame so plugins like clan.py can attach the clan first.
    def handle_player_loaded(self, player):
        if player.clan == self.clanTag:
            self.clanMembers.append(player)
            if len(self.clanMembers) >= 1:
                self.keep_going = True
                self.pauseAnimation = False
                self.start_rotating()
    
    def handle_player_disconnect(self, player, reason):
        try:
            self.clanMembers.remove(player)
            if len(self.clanMembers) <= 1:
                self.keep_going = False
        except KeyError:
            return
        
    def initialise(self):
        for player in self.players():
            if player.clan == self.clanTag:
                self.clanMembers.append(player)

        if len(self.clanMembers) >= 1:
            self.keep_going = True
            self.pauseAnimation = False
            self.start_rotating()
                
    @minqlx.thread
    def start_rotating(self):
        while True:
            # Make sure we're still supposed to run, otherwise exit the while loop.
            if (len(self.clanMembers) == 0 or self.keep_going == False):
                break
            for text in self.clanAnimation:
                # Make sure we're still supposed to run, otherwise exit the for loop.
                if (len(self.clanMembers) == 0 or self.keep_going == False):
                    break

                # Pause the loop during a map change etc.
                if self.pauseAnimation == True:
                    break
                
                # Set the clan tag to the next animation in the list.
                for p in self.clanMembers:
                    p.clan = text

                # Wait for a bit until we begin again.
                time.sleep(self.clanAnimationDelay)

    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4clanspinner.py^7 - version {}, created by Thomas Jones on 08/02/2016.".format(self.plugin_version))
