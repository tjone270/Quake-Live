# Created by Thomas Jones on 01/02/2016 - thomas@tomtecsolutions.com
# q3resolver.py, a plugin for minqlx to permit people to vote for Quake 3 maps.
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

import minqlx

class q3resolver(minqlx.Plugin):
    def __init__(self):
        self.add_hook("vote_called", self.handle_vote_called)
        self.add_command("tomtec_versions", self.cmd_showversion)
        self.plugin_version = "1.2"

        self.q3mapTranslationMapNamesQ3 = ["q3dm0", "q3dm1", "q3dm2", "q3dm3", "q3dm4", "q3dm5", "q3dm6", "q3dm7", "q3dm8", "q3dm9", "q3dm10", "q3dm11", "q3dm12", "q3dm13", "q3dm14", "q3dm15", "q3dm16", "q3dm17", "q3dm18", "q3dm19", "q3tourney1", "q3tourney2", "q3tourney3", "q3tourney4", "q3tourney5", "q3tourney6", "q3ctf1", "q3ctf2", "q3ctf3", "q3ctf4"]
        self.q3mapTranslationMapNamesQL = ["introduction", "arenagate", "spillway", "hearth", "eviscerated", "forgotten", "campgrounds", "retribution", "brimstoneabbey", "heroskeep", "namelessplace", "chemicalreaction", "dredwerkz", "lostworld", "grimdungeons", "demonkeep", "cobaltstation", "longestyard", "spacechamber", "terminalheights", "powerstation", "provinggrounds", "hellsgate", "verticalvengeance", "fatalinstinct", "beyondreality", "duelingkeeps", "troubledwaters", None, "spacectf"]
        self.q3mapTranslationLongNamesQ3 = ["Introduction", "Arena Gate", "House of Pain", "Arena of Death", "The Place of Many Deaths", "The Forgotten Place", "The Campgrounds", "Temple of Retribution", "Brimstone Abbey", "Hero's Keep", "The Nameless Place", "Deva Station", "The Dredwerkz", "Lost World", "Grim Dungeons", "Demon Keep", "The Bouncy Map", "The Longest Yard", "Space Chamber", "Apocalypse Void", "Power Station 0218", "The Proving Grounds", "Hell's Gate", "Vertical Vengeance", "Fatal Instinct", "The Very End of You", "Dueling Keeps", "Troubled Waters", "The Stronghold", "Space CTF"] 
        self.q3mapTranslationLongNamesQL = ["Introduction", "Arena Gate", "Spillway", "Hearth", "Eviscerated", "Forgotten", "Campgrounds", "Retribution", "Brimstone Abbey", "Hero's Keep", "Nameless Place", "Chemical Reaction", "Dredwerkz", "Lost World", "Grim Dungeons", "Demon Keep", "Cobalt Station", "Longest Yard", "Space Chamber", "Terminal Heights", "Power Station", "Proving Grounds", "Hell's Gate", "Vertical Vengeance", "Fatal Instinct", "Beyond Reality", "Dueling Keeps", "Troubled Waters", None, "Space CTF"]

    def handle_vote_called(self, caller, vote, args):
        if vote.lower() == "map":
            theArgs = args.lower().split()

            try:
                index = self.q3mapTranslationMapNamesQ3.index(theArgs[0])
            except ValueError:
                # The map which was callvoted is not in q3 translation list
                return

            q3mapName = str(self.q3mapTranslationMapNamesQ3[index])
            q3longName = str(self.q3mapTranslationLongNamesQ3[index])
            qLmapName = str(self.q3mapTranslationMapNamesQL[index])
            qLlongName = str(self.q3mapTranslationLongNamesQL[index])
            caller.tell("^1Q3A^7: Resolving Q3A map: ^1{}^7 (name: ^4{}^7) to QL map: ^4{}^7.".format(q3mapName, q3longName, qLlongName))
            
            if len(theArgs) == 2:
                # There's a factory appended to the map name, so re-call the vote with the specified factory.
                minqlx.client_command(caller.id, "callvote map {} {}".format(qLmapName, theArgs[1]))
            else:
                # No factory, proceed with re-calling the map vote only.
                minqlx.client_command(caller.id, "callvote map {}".format(qLmapName))
            return minqlx.RET_STOP_ALL
                
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4q3resolver.py^7 - version {}, created by Thomas Jones on 01/02/2016.".format(self.plugin_version))
