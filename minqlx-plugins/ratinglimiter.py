# Created by Thomas Jones on 27/02/16 - thomas@tomtecsolutions.com
# ratinglimiter.py, a plugin for minqlx to limit a server to players within certain ratings.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx
import requests
import time

class ratinglimiter(minqlx.Plugin):
    def __init__(self):
        self.add_hook("player_connect", self.handle_player_connected)
        self.add_hook("player_loaded", self.handle_player_loaded)
        self.add_hook("team_switch_attempt", self.handle_team_switch)
        self.add_hook("new_game", self.handle_new_game)

        self.add_command("tomtec_versions", self.cmd_showversion)

        self.set_cvar_once("qlx_minRating", "0")
        self.set_cvar_once("qlx_maxRating", "1600")
        self.set_cvar_once("qlx_kickPlayersOutOfRatingBounds", "1")

        self.set_cvar_once("qlx_balanceUrl", "qlstats.net:8080")
        self.set_cvar_once("qlx_balanceApi", "elo")

        self.prohibitedPlayers = []
        
        self.plugin_version = "1.1"


    def handle_new_game(self):
        self.prohibitedPlayers = [] # clear all banned players so their glickos can be recalculated.
        
    def handle_player_connected(self, player):
        if player in self.prohibitedPlayers:
            return "^1You are not permitted to join this server."
        
    @minqlx.thread
    def handle_player_loaded(self, player):
        try:
            url = "http://{}/{}/{}".format(self.get_cvar("qlx_balanceUrl"), self.get_cvar("qlx_balanceApi"), player.steam_id)
            res = requests.get(url)
            if res.status_code != requests.codes.ok:
                raise "Requests status code is not equal to 200 OK."
            js = res.json()
            gt = self.game.type_short
            if "players" not in js:
                raise "Strange data was retrieved, idk what the fuck's going on, leave me alone."
            for p in js["players"]:
                if int(p["steamid"]) == player.steam_id and gt in p:
                    self.process_player(player, p[gt]['elo'], p[gt]['games'])
                    
        except Exception as e:
            self.msg("^1{}: ^7{}".format(Exception, e))
            pass

    def handle_team_switch(self, player, old_team, new_team):
        if player in self.prohibitedPlayers:
            player.center_print("^1You are not permitted to join the game.")
            return minqlx.RET_STOP_ALL
        
    def process_player(self, player, glicko, games_played):
        if not self.get_cvar("qlx_kickPlayersOutOfRatingBounds", bool):
            return
        
        if glicko > self.get_cvar("qlx_maxRating", int): # player's glicko is higher than the server allows
            self.prohibitedPlayers.append(player)
            playerIs = "over"
        elif glicko < self.get_cvar("qlx_minRating", int): # player's glicko is lower than the server allows
            self.prohibitedPlayers.append(player)
            playerIs = "under"
        elif (glicko == self.get_cvar("qlx_minRating", int)) or (glicko == self.get_cvar("qlx_maxRating", int)): # player's glicko is the same as either of the limits
            player.tell("Your glicko ({}) is on the borderline of the server's glicko limits. Don't be surprised if you're kicked after some games.".format(glicko))
            return
        
        if player in self.prohibitedPlayers:
            if playerIs == "over": limit = self.get_cvar("qlx_maxRating", int)
            else: limit = self.get_cvar("qlx_minRating", int)
            player.mute()
            player.put("spectator")
            player.tell("Sorry, your glicko rating ({}) is {} the glicko limitation on this server ({}). ^1You will be kicked shortly.".format(glicko, playerIs, limit))
            time.sleep(8)
            player.kick("Your glicko rating was {} the server limitation ({}).".format(playerIs, limit))
            
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4ratinglimiter.py^7 - version {}, created by Thomas Jones on 27/02/2016.".format(self.plugin_version))
