# Created by Thomas Jones on 22/05/2016 - thomas@tomtecsolutions.com
# aliases.py, a plugin for minqlx to show aliases from the redis database.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

# Player selection system for short-mid-long range weapon distribution created by zlr.
# http://pastebin.com/B8Ruq1YM - PREVIOUS
# http://pastebin.com/Tse5dkEi - CURRENT


GAMEMODE_NAME = "Tri-Weapon CA"
CALLVOTE_STRING = "triweapon"
SUPPORTED_GAMETYPES = ("ca")


import minqlx, random
class gamemode_triweapon(minqlx.Plugin):
    def __init__(self):
        self.add_hook("player_loaded", self.handle_player_loaded, priority=minqlx.PRI_LOW)
        self.add_hook("vote_called", self.handle_vote_called)
        self.add_hook("unload", self.handle_plugin_unload)
        self.add_command((self.__class__.__name__), self.cmd_gamemode_switch, 5, usage="on/off")
        self.add_command("tomtec_versions", self.cmd_showversion)
        self.gamemode_active = False

######### define your hooks/commands/stuff below
        self.plugin_version = "1.2"
        self.add_hook("round_countdown", self.handle_round_countdown)

        self.CLOSE_RANGE_HEALTH = 200
        self.CLOSE_RANGE_ARMOUR = 100

        self.MID_RANGE_HEALTH = 150
        self.MID_RANGE_ARMOUR = 100
 
        self.LONG_RANGE_HEALTH = 100
        self.LONG_RANGE_ARMOUR = 100
    
    @minqlx.next_frame
    def handle_round_countdown(self, *args, **kwargs): 
        if self.gamemode_active == True:
            for team in self.teams(): # cycle through teams, red, blue, specs, free (free team is the team that players are placed into in team-less gametypes (eg. FFA))
                if (team != "spectator") and (team != "free"): # don't want to be giving weapons to players in the spectator/free teams, will likely crash server.
                    teams = self.teams() # copy the teams dictionary so we don't try to modify the original
                    teamsize = len(teams['red'])
                    close_range_counter = 1
                    mid_range_counter = 1
                    long_range_counter = 1
                    if (teamsize == 2):
                        close_range_cap = 1
                        mid_range_cap = 1
                        long_range_cap = 1
                    elif (teamsize == 3):
                        close_range_cap = 1
                        mid_range_cap = 1
                        long_range_cap = 1
                    elif (teamsize == 4):
                        close_range_cap = 2
                        mid_range_cap = 1
                        long_range_cap = 1
                    elif (teamsize == 5):
                        close_range_cap = 2
                        mid_range_cap = 2
                        long_range_cap = 1
                    elif (teamsize == 6):
                        close_range_cap = 2
                        mid_range_cap = 2
                        long_range_cap = 2
                    elif (teamsize == 7):
                        close_range_cap = 3
                        mid_range_cap = 2
                        long_range_cap = 2
                    elif (teamsize == 8):
                        close_range_cap = 3
                        mid_range_cap = 3
                        long_range_cap = 2
                    theTeam = teams[team]
                    random.shuffle(theTeam)
                    for player in theTeam:
                        random_int = random.randint(1,3)
                        if random_int == 1:
                            if close_range_counter <= close_range_cap:
                                player.weapons(reset=True, g=True, rl=True, gl=True, mg=True) 
                                player.health = self.CLOSE_RANGE_HEALTH 
                                player.armor = self.CLOSE_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^1SHORT-RANGE WEAPONS")
                                player.weapon(5)
                                close_range_counter += 1
                            elif mid_range_counter <= mid_range_cap:
                                player.weapons(reset=True, g=True, lg=True, sg=True, hmg=True)
                                player.health = self.MID_RANGE_HEALTH 
                                player.armor = self.MID_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^3MID-RANGE WEAPONS")
                                player.weapon(2)
                                mid_range_counter += 1
                            elif long_range_counter <= long_range_cap:
                                player.weapons(reset=True, g=True, rg=True, sg=True, pg=True) 
                                player.health = self.LONG_RANGE_HEALTH 
                                player.armor = self.LONG_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^2LONG-RANGE WEAPONS")
                                player.weapon(7)
                                long_range_counter += 1
                        elif random_int == 2:
                            if mid_range_counter <= mid_range_cap:
                                player.weapons(reset=True, g=True, lg=True, sg=True, hmg=True)
                                player.health = self.MID_RANGE_HEALTH 
                                player.armor = self.MID_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^3MID-RANGE WEAPONS")
                                player.weapon(2)
                                mid_range_counter += 1
                            elif long_range_counter <= long_range_cap:
                                player.weapons(reset=True, g=True, rg=True, sg=True, pg=True) 
                                player.health = self.LONG_RANGE_HEALTH 
                                player.armor = self.LONG_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^2LONG-RANGE WEAPONS")
                                player.weapon(7)
                                long_range_counter += 1
                            elif close_range_counter <= close_range_cap:
                                player.weapons(reset=True, g=True, rl=True, gl=True, mg=True) 
                                player.health = self.CLOSE_RANGE_HEALTH 
                                player.armor = self.CLOSE_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^1SHORT-RANGE WEAPONS")
                                player.weapon(5)
                                close_range_counter += 1
                        else:
                            if long_range_counter <= long_range_cap:
                                player.weapons(reset=True, g=True, rg=True, sg=True, pg=True) 
                                player.health = self.LONG_RANGE_HEALTH 
                                player.armor = self.LONG_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^2LONG-RANGE WEAPONS")
                                player.weapon(7)
                                long_range_counter += 1
                            elif mid_range_counter <= mid_range_cap:
                                player.weapons(reset=True, g=True, lg=True, sg=True, hmg=True)
                                player.health = self.MID_RANGE_HEALTH 
                                player.armor = self.MID_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^3MID-RANGE WEAPONS")
                                player.weapon(2)
                                mid_range_counter += 1
                            elif close_range_counter <= close_range_cap:
                                player.weapons(reset=True, g=True, rl=True, gl=True, mg=True) 
                                player.health = self.CLOSE_RANGE_HEALTH 
                                player.armor = self.CLOSE_RANGE_ARMOUR 
                                player.center_print("Weapon Assignment:\n^1SHORT-RANGE WEAPONS")
                                player.weapon(5)
                                close_range_counter += 1
            
    def housekeeping_tasks(self): # runs when the plugin unloads and when the mode is call-voted off
        # looks like we have nothing to do...
        return

        
### Don't touch the below, it morphs to your code:
    def handle_plugin_unload(self, plugin):
        if plugin == (self.__class__.__name__):
            self.gamemode_active == False
            self.housekeeping_tasks()
            
    def cmd_gamemode_switch(self, player, msg, channel):
        if len(msg) < 2:
            return minqlx.RET_USAGE
        
        if msg[1].lower() == "on":
            self.gamemode_active = True
        elif msg[1].lower() == "off":
            self.gamemode_active = False
            self.housekeeping_tasks()
        else:
            return minqlx.RET_USAGE
    
    def handle_vote_called(self, caller, vote, args):
        if not (self.get_cvar("g_allowSpecVote", bool)) and caller.team == "spectator":
            if caller.privileges == None:
                caller.tell("You are not allowed to call a vote as spectator.")
                return minqlx.RET_STOP_ALL

        if vote.lower() == "gamemode":
            if args.split()[0].lower() == CALLVOTE_STRING:
                if len(args.split()) <= 1:
                    caller.tell("^2/cv gamemode {} [on/off]^7 is the usage for this callvote gamemode command.".format(CALLVOTE_STRING))
                elif (args.split()[1].lower() == "on") or (args.split()[1].lower() == "off"):
                    if self.game.type_short in SUPPORTED_GAMETYPES:
                        self.callvote("qlx !{} {}".format(self.__class__.__name__, args.split()[1].lower()), "gamemode {}: {}".format(GAMEMODE_NAME, args.split()[1].lower()))
                        self.msg("{}^7 called a vote.".format(caller.name))
                    else:
                        caller.tell("The ^4{}^7 gamemode is not supported on this gametype.".format(GAMEMODE_NAME))
                else:
                    caller.tell("^2/cv gamemode {} [on/off]^7 is the usage for this callvote gamemode command.".format(CALLVOTE_STRING))

                return minqlx.RET_STOP_ALL
            
    @minqlx.delay(3)
    def handle_player_loaded(self, player):
        if self.gamemode_active == True:
            player.tell("This server has ^4{}^7 mode enabled. To disable it, use ^2/cv gamemode {} off^7.".format(GAMEMODE_NAME, CALLVOTE_STRING))

    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4{}.py^7 - version {}, created by Thomas Jones on 22/05/2016.".format(self.__class__.__name__, self.plugin_version))

        
        
