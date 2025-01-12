# Minqlx Plugins
## Plugin Descriptions and Usages:


### `aliases.py`
Shows player aliases from the Redis database. Aliases are recorded on player connect. The plugin does not have to be loaded to record aliases.
```
Commands:
    !alias <id>           - List aliases used by the player.
    !clearaliases         - Clear all player aliases from the database.
```

### `autorestart.py`
Automatically runs the `quit` command on a server at XX:XX time, if no-one's connected to the server.
If you use Supervisor (process manager) with the `autorestart` parameter, the server will automatically relaunch after the `quit` command runs.
```
CVARs:
    qlx_autoRestartTime         - The time for the server to quit automatically in 24-hour time syntax.
        Default: 00:00

Guide:
    autorestart.py requires the 'schedule' python library to be installed. You can install it with the following command:
        sudo python3.5 -m pip install schedule
```

### `botmanager.py`
Adds a `/cv addbot | !addbot` and `/cv rembot | !rembot` command system. Has functionality to automatically adds/removes bots to even teams. Also displays a warning on maps that don't support bots.  
It's a good idea to set `bot_enable` to `1` by default, otherwise the plugin's useless.
```
CVARs:
    bot_autoManage        - Automatically add/remove bot to even up the teams. Will disable all other commands during automatic management.
        Default: 0

Commands:
    !addbot               - Adds a bot.
    !rembot               - Removes a bot.

Client Commands:
    /cv addbot            - Vote to add a bot.
    /cv rembot            - Vote to remove a bot.
```

### `branding.py`
Replaces in-game messages/text with custom text set in special CVARs.
```
CVARs:
    qlx_serverBrandName              - Where the map name usually appears, the text set in this cvar will appear instead.
    qlx_serverBrandTopField          - Where the map author credit (line 1) appears, the text set in this cvar will appear after the credit.
    qlx_serverBrandBottomField       - Where the map author credit (line 2) appears, the text set in this cvar will appear after the credit.

    qlx_connectMessage               - When the player is at the initial connect screen when they first connect, text will appear here.
    qlx_loadedMessage                - Causes text to appear in the middle of the screen on each new map load.
    qlx_countdownMessage             - When the countdown begins, this text will appear mid-screen. (like the qlx_loadedMessage does)
    qlx_endOfGameMessage             - When the game finishes, it'll put the text in this cvar in the text box on the left.

    qlx_brandingPrependMapName       - This cvar will put the map name before your qlx_serverBrandName.                     
        Default: 0
    qlx_brandingAppendGameType       - Will add the game type after your qlx_serverBrandName.                               
        Default: 0
    qlx_rainbowBrandName             - Make the entire map name (qlx_serverBrandName) appear in rainbow colouring.          
        Default: 0
```

### `changemap.py`
Changes the map/factory when the last person leaves the server.
```
CVARs:
    qlx_defaultMapToChangeTo                - The map to change to.
        Default: 'campgrounds'
    qlx_defaultMapFactoryToChangeTo         - The factory to change to.
        Default: 'ffa'
```

### `commlink.py`
Provides a platform for inter-server communication.
```
Commands:
    !commlink                              - Enables/disables CommLink messages for players that do/do not want to see the messages.
    !world <message>                       - Sends the message to all other servers in the same CommLink identity group.

CVARs:
    qlx_commlinkIdentity                   - Set this to something unique, it defines your CommLink group.
        No Default.                          (this CVAR must be the same across all servers)
    qlx_commlinkServerName                 - The name of the server (appears before CommLink messages).
        Default: Server-XXXX
    qlx_enableConnectDisconnectMessages    - Enables the 'Player connected.' and 'Player disconnected.' messages.
        Default: 1
    qlx_enableCommlinkMessages             - Default behaviour of !commlink command.
        Default: 1
```

### `custom_votes.py`
Adds extra vote functionality.
Votes are listed [here](http://tomtecsolutions.com.au/thepurgery/index.php?title=Special_votes).
```
CVARs:
    qlx_rulesetLocked                      - Disables `/cv ruleset` votes.
        Default: 0
    qlx_disablePlayerRemoval               - Prevents `/cv kick` and `/cv tempban` votes for non-privileged players.
        Default: 0
    qlx_disableCvarVoting                  - Disables `/cv cvar` server votes.
        Default: 1
    qlx_cvarVotePermissionRequired         - Required permission level to call a CVAR vote.
        Default: 3
```

### `dictionary.py`
Defines english words, and produces random english words upon command.
```
Commands:
    !define <word>           - Define an english word(s).
    !randomword              - Produce a random english word.
```

### `disabled_commands.py`
Displays a message when a command listed in the disabled commands list is run, and stops the command from running in the first place.
```
Guide:
    Open the plugin up in an editor and edit the DISABLED_COMMANDS array, adding commands to the list (omitting the !).
    Save and load to a minqlx-enabled Quake server and you'll find the commands in the array no longer run.
```
   
### `permaban.py`
Permanently bans players from the server. Cross-references SteamIDs with IP addresses for a more through ban.  
Permabans can't be undone without a lot of DB modification.
```
Commands:
    !permaban <id>           - Permanently bans <id> from the server.
```

### `permissionlist.py`
Lists all players in the minqlx database with a permission level greater than 0. Command functions for permission level 5 players only.

```
Commands:
    !permissionlist          - Get the list.
```

### `ips.py`
Shows player IP address history from the Redis database. IPs are recorded on player connect. The plugin does not have to be loaded to record IPs.
```
Commands:
    !ip <id>           - List IP addresses used by the player.
```

### `onjoin.py`
Displays a saved message from a player when they connect to a server.
```
Commands:
    !onjoin <message>           - Set an onjoin message (run without arguments to clear message).
```

### `q3resolver.py`
Permits players to call-vote Quake III map names.
The plugin will resolve the Quake III map name to the Quake Live equivalent.
```
Usage:
    /cv map q3dm12

Result:
    Map-vote is called for map Dredwerkz.
```

### `quiet.py`
Prevents people from using text-based chat during matches.
```
CVARs:
    qlx_permitChatDuringWarmup          - Allows chat during warmup.
        Default: 1
    qlx_permLevelRequiredToTalk         - Permission level required to use text chat.
        Default: 4
```

### `ratinglimiter.py`
Limits a server to players who can only play if they're within certain glicko-rating limits.
```
CVARs:
    qlx_minRating                           - Minimum rating limit.
        Default: 0
    qlx_maxRating                           - Maximum rating limit.
        Default: 1600
    qlx_kickPlayersOutOfRatingBounds        - Kick players that don't conform to the rating limits.
        Default: 1
```

### `sv_fps.py`
Provides a safe way to modify the server frame-rate variable.  
Rules:
1. sv_fps must be greater than or equal to 40.
2. sv_fps can't be a negative number.
3. sv_fps must be divisable by 40.
```
Commands:
    !sv_fps/!svfps <int>   - Sets the sv_fps cvar live in the server.

CVARs:
    qlx_svfps              - Set this cvar to your desired sv_fps value, and the server will set it upon loading the plugin.
        Default: 40
```

### `thirtysecwarn.py`
Plays unused VO when a game is nearing the round time limit.

### `votemanager.py`
Permits players with Minqlx Permission level 3 to vote and force-vote.
Requires the players in question to not have QLDS admin/mod.
```
Usage:
    A vote is called.
    Player with permlevel 3 or above presses F1/F2 once. Pressing F1/F2 a second time forces the vote.
```

### `votestats.py`
De-anonymises votes and provides messages about map changes after the map-vote/vote results.
```
Commands:
    !votes                        - Hides the 'Player voted yes/no.' messages for the player running the command.

CVARs:
    qlx_privatiseVotes            - Enabling this renders the plugin useless, apart from vote results and map change messages.
        Default: 0
```
