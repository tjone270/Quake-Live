# This file is part of the Quake Live server implementation by TomTec Solutions. Do not copy or redistribute or link to this file without the emailed consent of Thomas Jones (thomas@tomtecsolutions.com).

import minqlx

class q3audio(minqlx.Plugin):
    def __init__(self):
        self.add_hook("map", self.map_load)
        self.add_hook("vote_started", self.handle_vote_started)
        self.add_hook("vote_ended", self.handle_vote_ended)
        self.add_hook("game_countdown", self.handle_game_countdown)
        self.add_hook("game_start", self.handle_game_start)
        self.add_hook("game_end", self.handle_game_end)
        self.add_hook("round_countdown", self.handle_round_countdown)
        self.add_hook("round_start", self.handle_round_start)
        self.add_hook("round_end", self.handle_round_end)
        self.add_command("tomtec_versions", self.cmd_showversion)

        self.team_gametypes = ["tdm", "ca", "ctf", "1f", "har", "ft", "dom", "ad", "rr"]
        self.free_gametypes = ["ffa", "duel", "race"]

        self.stored_score_red = 0
        self.stored_score_blue = 0
        
        self.plugin_version = "0.1"

        self.isFirstRound = True
            
    def map_load(self, *args, **kwargs):
        self.game.workshop_items += [614429927]

    def handle_vote_started(self, *args, **kwargs):
        @minqlx.next_frame
        def vote_now():
            self.stop_sound()
            self.play_sound("q3_audio/vo/vote/vote_now.wav")
        vote_now()
        
    def handle_vote_ended(self, votes, vote, args, passed):
        @minqlx.delay(1.2)
        def f():
            self.stop_sound()
        f()
        if passed:
            self.play_sound("q3_audio/vo/vote/vote_passed.wav")
        else:
            self.play_sound("q3_audio/vo/vote/vote_failed.wav")
            
    def handle_game_countdown(self, *args, **kwargs):
        if self.game.type_short in self.team_gametypes:
            @minqlx.next_frame
            def prepare_your_team():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/prepare_your_team.wav")
            prepare_your_team()
        elif self.game.type_short in self.free_gametypes:
            @minqlx.next_frame
            def prepare_to_fight():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/prepare_to_fight.wav")
            prepare_to_fight()

            @minqlx.delay(7)
            def three():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/3.wav")
            three()

            @minqlx.delay(8)
            def two():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/2.wav")
            two()

            @minqlx.delay(9)
            def one():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/1.wav")
            one()


    def handle_round_countdown(self, *args, **kwargs):
        if self.isFirstRound:
            self.isFirstRound = False
            @minqlx.delay(4.6)
            def stop_round_begins_in():
                self.stop_sound()
            stop_round_begins_in()

            @minqlx.delay(6.6)
            def three():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/3.wav")
            three()

            @minqlx.delay(7.6)
            def two():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/2.wav")
            two()

            @minqlx.delay(8.6)
            def one():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/1.wav")
            one()
        else:
            @minqlx.delay(5)
            def stop_round_begins_in():
                self.stop_sound()
            stop_round_begins_in()

            @minqlx.delay(7)
            def three():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/3.wav")
            three()

            @minqlx.delay(8)
            def two():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/2.wav")
            two()

            @minqlx.delay(9)
            def one():
                self.stop_sound()
                self.play_sound("q3_audio/vo/gamestates/countdown/1.wav")
            one()
        
    def handle_round_start(self, *args, **kwargs):
        @minqlx.next_frame
        def fight():
            self.stop_sound()
            self.play_sound("q3_audio/vo/gamestates/countdown/F.wav")
        fight()

    def handle_round_end(self, *args, **kwargs):
        if self.game.type_short in self.team_gametypes:
            if self.game.red_score != self.stored_score_red:
                self.stored_score_red = self.game.red_score
                self.stop_sound()
                self.play_sound("q3_audio/vo/teamgame/red_scores.wav")
            elif self.game.blue_score != self.stored_score_blue:
                self.stored_score_blue = self.game.blue_score
                self.stop_sound()
                self.play_sound("q3_audio/vo/teamgame/blue_scores.wav")
            
        
    def handle_game_start(self, *args, **kwargs):
        self.stored_score_red = self.game.red_score
        self.stored_score_blue = self.game.blue_score
        self.isFirstRound = True
        if self.game.type_short in self.free_gametypes:
            self.stop_sound()
            self.play_sound("q3_audio/vo/gamestates/countdown/F.wav")
            
    def handle_game_end(self, *args, **kwargs):
        if self.game.type_short == "duel":
            teams = self.teams()
            free_team = teams["free"]
            score1 = free_team[0].score
            player1 = self.player(free_team[0].id)
            score2 = free_team[1].score
            player2 = self.player(free_team[1].id)
            if score1 > score2:
                @minqlx.next_frame
                def conclusion():
                    self.stop_sound()
                    self.play_sound("q3_audio/vo/gamestates/you_win.wav", player1)
                    self.play_sound("q3_audio/vo/gamestates/you_lose.wav", player2)
                conclusion()
            elif score2 > score1:
                @minqlx.next_frame
                def conclusion():
                    self.stop_sound()
                    self.play_sound("q3_audio/vo/gamestates/you_win.wav", player2)
                    self.play_sound("q3_audio/vo/gamestates/you_lose.wav", player1)
                conclusion()
            
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4q3audio.py^7 - version {}, created by Thomas Jones on 03/02/2016.".format(self.plugin_version))
