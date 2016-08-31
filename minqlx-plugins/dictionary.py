# Created by Thomas Jones on 22/08/2016 - thomas@tomtecsolutions.com
# dictionary.py - a minqlx plugin to define english words and produce random words
# This plugin is released to everyone, for any purpose. It comes with no warranty, no guarantee it works, it's released AS IS.
# You can modify everything, except for lines 1-4 and the !tomtec_versions code. They're there to indicate I whacked this together originally. Please make it better :D

DICT_API_URL = "https://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase={}"
WORD_API_URL = "http://setgetgo.com/randomword/get.php"

import minqlx, requests, json
class dictionary(minqlx.Plugin):
    def __init__(self):
        self.add_command("define", self.cmd_define_term, usage="<term>")
        self.add_command(("randomword", "randword"), self.cmd_random_word)
        self.add_command("tomtec_versions", self.cmd_showversion)

        self.plugin_version = "1.2"
        
    
    def cmd_define_term(self, player, msg, channel):
        @minqlx.thread
        def run(player, msg, channel):
            dictData = requests.get(DICT_API_URL.format("%20".join(msg[1:])), stream=True)
            jsonDict = json.loads(str(dictData.text))
            try:
                channel.reply("^4Definition^7: {}^7".format(jsonDict["tuc"][0]["meanings"][0]["text"]))
            except Exception:
                channel.reply("^4Definition: ^1NO DEFINITIONS FOUND^7")
            
        if len(msg) < 2:
            return minqlx.RET_USAGE
        else:
            run(player, msg, channel)

    @minqlx.thread
    def cmd_random_word(self, player, msg, channel):
        word = requests.get(WORD_API_URL, stream=True)
        channel.reply("^4Random Word^7: {}^7.".format(word.text))
        
    def cmd_showversion(self, player, msg, channel):
        channel.reply("^4dictionary.py^7 - version {}, created by Thomas Jones on 22/08/16.".format(self.plugin_version))

        
