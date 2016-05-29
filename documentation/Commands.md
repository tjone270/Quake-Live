# Quake Live Technical Documentation

## Local/Builtin
| Command | Description | Syntax | Client | Server |
| :------ | :---------: | ------ | :----: | :----: |
|aclear|?
|arena|Load a sp_arena file.|`arena <arena file>`|:white_check_mark:|:white_check_mark:
|astatus|?
|bind|Bind a key to a command/alias.|`bind <key> <command/alias>`|:white_check_mark:|:x:
|bindlist|List all key binds currently set/assigned.|`bindlist`|:white_check_mark:|:x:
|centerview|Centers the vertical view pitch of the player.|`centerview`|:white_check_mark:|:x:
|changeVectors|Prints out a table from the current statistics for development usage.|`changevectors`|:white_check_mark:|:x:
|clear|Clear the console scrollback.|`clear`|:white_check_mark:|:x:
|clearcvar|Clears the specified CVAR's value, setting it to Null ("")|`clearcvar <cvar>`|:white_check_mark:|:white_check_mark:
|clientfriendinvite|Send a Steam friend invite to the specified player.|`clientfriendinvite <client id>`|:white_check_mark:|:x:
|clientinfo|Prints your state, current server if any and userinfo strings.|`clientinfo`|:white_check_mark:|:x:
|clientkick|Kicks a player/bot by client ID|`clientkick <client id>`|:white_check_mark:|:white_check_mark:
|clientviewprofile|Opens the Steam overlay with the Steam profile of the player specified in a browser window.|`clientviewprofile <client id>`|:white_check_mark:|:x:
|cmdlist|Alias of `listcmds`.
|condump|Dump all buffered text in the console to a file (with LF line endings).|`condump <file>`|:white_check_mark:|:x:
|configstrings|Lists current config-strings from the server in index order.|`configstrings`|:white_check_mark:|:x:
|connect|Connect to a server. Accepts domains and IP addresses (requires port).|`connect <ip/domain>:<port>`|:white_check_mark:|:x:
|connect_lobby|?|`connect_lobby`|:white_check_mark:|:x:
|cvarlist|Alias of `listcvars`.
|cvar_restart|Restarts the CVAR subsystem. Note that this clears most changes to CVARs.|`cvar_restart`|:white_check_mark:|:white_check_mark:
|demo|Play a demo file.|`demo <file>`|:white_check_mark:|:x:
|devmap|Loads a map in development/cheats mode. Will append a `cheats` tag to your server while in devmap mode.|`devmap <map> [factory]`|:white_check_mark:|:white_check_mark:
|dir|List the contents of a directory.|`dir <directory> [extension]`|:white_check_mark:|:white_check_mark:
|disconnect|Disconnect from the current server.|`disconnect`|:white_check_mark:|:x:
|dumpuser|Prints the player's `userinfo` to the console.|`dumpuser <player name>`|:white_check_mark:|:white_check_mark:
|echo|Prints text to console.|`echo <text>`|:white_check_mark:|:white_check_mark:
|exec|Executes a configuration file.|`exec <config file>`|:white_check_mark:|:white_check_mark:
|fdir|List files that match a specified filter in the search path.|`fdir <filter>`|:white_check_mark:|:white_check_mark:
|find|Searches the console history for text (case-sensitive).|`find <string>`|:white_check_mark:|:x:
|fs_openedList|Lists currently opened PK3 archives.|`fs_openedlist`|:white_check_mark:|:x:
|fs_referencedList|Lists currently referenced PK3 archive names.|`fs_referencedlist`|:white_check_mark:|:x:
|gfxinfo|Displays graphics subsystem information, including card vendor, renderer etc.|`gfxinfo`|:white_check_mark:|:x:
|imagelist|Lists currently loaded images.|`imagelist`|:white_check_mark:|:x:
|in_restart|Restarts the game input subsystem.|`in_restart`|:white_check_mark:|:x:
|kick|Kick a player by name.|`kick <player name>`|:white_check_mark:|:white_check_mark:
|killserver|Unload the currently loaded map and put the server in a 'map-less' state (does not exit the process but shuts down the game, further `map` commands can be run to recover the server)|`killserver`|:white_check_mark:|:white_check_mark:
|listcmds|Lists all commands with optional filtering.|`listcmds [filter]`|:white_check_mark:|:white_check_mark:
|listcvars|Lists all CVARs with optional filtering.|`listcvars [filter]`|:white_check_mark:|:white_check_mark:
|ListInputDevices|Lists all input devices.|`listinputdevices`|:white_check_mark:|:x:
|map|Loads a map normally.|`map <map name> [factory]`|:white_check_mark:|:white_check_mark:
|map_restart|Reloads the map, it's entities and respawns all players.|`map_restart`|:white_check_mark:|:white_check_mark:
|meminfo|Shows memory allocation information.|`meminfo`|:white_check_mark:|:white_check_mark:
|messagemode|Calls the `say` chat dialog.|`messagemode`|:white_check_mark:|:x:
|messagemode2|Calls the `say_team` chat dialog.|`messagemode`|:white_check_mark:|:x:
|midiinfo|Display MIDI device information.|`midiinfo`|:white_check_mark:|:x:
|model|Get/set the current player model/skin.|`model [model/skin]`|:white_check_mark:|:x:
|modelist|Display a list of monitor configurations that `r_mode` will accept.|`modelist`|:white_check_mark:|:x:
|modellist|A list of all model files currently loaded/in use.|`modellist`|:white_check_mark:|:x:
|music|Plays a looping music track in-game.|`music <path to music file> [loop file]`|:white_check_mark:|:x:
|net_restart|Restarts the networking subsystem.|`net_restart`|:white_check_mark:|:x:
|path|Show the current paths in the search path and whether or not those files are pure. Also show currently opened files (handles).|`path`|:white_check_mark:|:white_check_mark:
|play|Plays a sound in-game.|`play <path to sound file>`|:white_check_mark:|:x:
|postprocess_restart|Restarts the post-processing subsystem.|`postprocess_restart`|:white_check_mark:|:x:
|quit|Exits the client/server process immediately and shuts down the game.|`quit`|:white_check_mark:|:white_check_mark:
|reconnect|Reconnect to the last server you were connected to. If you're connected to a server, it'll reconnect to your current server.|`reconnect`|:white_check_mark:|:x:
|record|Records a demo in-game.|`record <file name>`|:white_check_mark:|:x:
|reload_arenas|Reloads the arena definitions (`.arenas`)|`reload_arenas`|:white_check_mark:|:white_check_mark:
|reload_factories|Reloads all the factories (will read in new factories) from pak00.pk3/scripts/factories.txt and scripts/*.factories|`reload_factories`|:white_check_mark:|:white_check_mark:
|reload_mappool|Reloads the map-pool file specified in the `sv_mappoolFile` CVAR.|`reload_mappool`|:white_check_mark:|:white_check_mark:
|reset|Resets a CVAR to it's initial value.|`reset <cvar>`|:white_check_mark:|:white_check_mark:
|say|Send a message from the client/server. Server messages are prefixed with `Server: `, client messages are prefixed with `PlayerName: ^2 `|`say <message>`|:white_check_mark:|:white_check_mark:
|screenshot|Write a screenshot in TGA format.|`screenshot [file name]`|:white_check_mark:|:x:
|screenshotJPEG|Write a screenshot in JPEG format.|`screenshotjpeg [file name]`|:white_check_mark:|:x:
|sectorlist|List the map's sectors and the number of entities within the sectors.|`sectorlist`|:white_check_mark:|:white_check_mark:
|serverinfo|Displays all CVARs with flag 64 set. These CVARs can be queried via the Valve source protocol from the server's `net_port`.|`serverinfo`|:white_check_mark:|:white_check_mark:
|setenv|Mostly used for setting/controlling Voodoo environment variables. Very likely unused and won't do anything now.|`setenv`|:white_check_mark:|:x:
|shaderlist|List all shaders currently loaded.|`shaderlist`|:white_check_mark:|:x:
|showip|Display current IP address(es).|`showip`|:white_check_mark:|:x:
|s_info|Display sound/audio system information.|`s_info`|:white_check_mark:|:x:
|skinlist|List loaded 'skins' for the currently selected player model.|`skinlist`|:white_check_mark:|:x:
|s_list|List all currently loaded/buffered sound files.|`s_list`|:white_check_mark:|:x:
|snd_restart|Restarts the audio subsystem.|`snd_restart`|:white_check_mark:|:x:
|s_stop|Stop playing the looping music track.|`s_stop`|:white_check_mark:|:x:
|startRandomMap|Runs a random map listed in the map-pool file (with the factory also specified). By default this runs on server start-up unless specified otherwise.|`startRandomMap`|:white_check_mark:|:white_check_mark:
|status|List all clients, and their Client IDs, scores, latency in milliseconds (ping), in-game name, lastmsg, IP address, QPort, player rate and Steam64 ID.|`status`|:white_check_mark:|:white_check_mark:
|steam_downloadugc|Download a Steam workshop item.|`steam_downloadugc <workshop id>`|:white_check_mark:|:x:
|steam_subscribeugc|Subscribe to a Steam workshop item.|`steam_subscribeugc <workshop id>`|:white_check_mark:|:x:
|steam_unsubscribeugc|Unsubscribe from a Steam workshop item.|`steam_unsubscribeugc <workshop id>`|:white_check_mark:|:x:
|stoprecord|Stops recording a demo.|`stoprecord`|:white_check_mark:|:x:
|toggleconsole|Toggles the console into/out of view. Designed for binding.|`toggleconsole`|:white_check_mark:|:x:
|touchFile|Opens the specified file for reading and then immediately closes the file again.|`touchfile <file>`|:white_check_mark:|:white_check_mark:
|unalias|Remove a single alias.|`unalias <alias>`|:white_check_mark:|:x:
|unaliasall|Removes all set aliases.|`unaliasall`|:white_check_mark:|:x:
|unbind|Removes a single bind on a key.|`unbind <key>`|:white_check_mark:|:x:
|unbindall|Removes all set binds. Usually used within `repconfig.cfg`/`qzconfig.cfg`.|`unbindall`|:white_check_mark:|:x:
|userinfo|?|`userinfo`|:white_check_mark:|:x:
|vid_restart|Restarts the graphics subsystem.|`vid_restart`|:white_check_mark:|:x:
|web_changeHash|?|`web_changeHash <hash>`|:white_check_mark:|:x:
|web_clearCache|Clears the Awesomium browser web-cache.|`web_clearcache`|:white_check_mark:|:x:
|web_hideBrowser|Hides the web-based UI.|`web_hidebrowser`|:white_check_mark:|:x:
|web_reload|For development use only. Will trap your client in the old Quake 3 Arena menu system, requires a relaunch to get back to normal functionality|`web_reload`|:white_check_mark:|:x:
|web_showBrowser|Shows the web-based UI (even when in a match).|`web_showbrowser`|:white_check_mark:|:x:
|web_showError|Displays a error message in the web-based UI.|`web_showerror <error message>`|:white_check_mark:|:x:
|writeClientConfig|Writes a new configuration file that doesn't include game or server CVARs or any default settings.|`writeclientconfig <file>`|:white_check_mark:|:white_check_mark:
|writeconfig|Writes a new configuration file with all currently set CVARs and binds.|`writeconfig <file>`|:white_check_mark:|:white_check_mark:

## Scripting
| Command | Description | Syntax | Client | Server |
| :------ | :---------: | ------ | :----: | :----: |
|alias|Create a command alias.|`alias <alias name> <command to alias>`|:white_check_mark:|:x:
|cmd|Executes a command.|`cmd <command>`|:white_check_mark:|:x:
|cvarAdd|Adds/subtracts an int/float stored in a CVAR.|`cvaradd <cvar> <+/- value>`|:white_check_mark:|:white_check_mark:
|cvarMult|Multiplies an int/float stored in a CVAR.|`cvarmult s_volume 5`|:white_check_mark:|:white_check_mark:
|set|Sets a CVAR with no special flags set.|`set <cvar> <value>`|:white_check_mark:|:white_check_mark:
|seta|Sets a CVAR with the archive flag set.|`seta <cvar> <value>`|:white_check_mark:|:white_check_mark:
|toggle|Inverts a CVAR's boolean value.|`toggle <cvar>`|:white_check_mark:|:white_check_mark:
|vstr|Executes commands within a CVAR.|`vstr <cvar>`|:white_check_mark:|:white_check_mark:
|wait|Waits for one frame (or specified frames) before continuing.|`wait [frames]`|:white_check_mark:|:x:

## Server>Client commands
#### This list will only contain commands that are understood and are utilised by mods and is therefore lacking with other commands that aren't understood (`tinfo`, etc)
| Command | Description | Syntax |
| :------ | :---------: | ------ |
|cp|Centre-prints text to the middle of the client's screen. Accepts newline control characters.|`cp <text>`
|cs|Set a config-string on the client.|`cs <index> <value>`
|print|Prints text to the client's console/on-screen message feed.|`print <text>`
|disconnect|Disconnect a client from the server. Utilised by the server when kicking clients etc.|`disconnect "[message to display to client]"`
|playMusic|Play a looping music file on the client.|`playMusic <music file>`
|playSound|Play a sound file on the client.|`playSound <sound file>`
|scores(_??)|Sends scores data to the client.|?

## Client>Server commands
#### This list will only contain commands that are understood. Modified servers can create new client commands and intercept existing ones.
| Command | Description | Syntax |
| :------ | :---------: | ------ |
|callvote|Calls a vote.|`callvote <vote> <args>`
|cv|Alias of `callvote`.
|god|Toggles god-mode (invulnerability to most damage).|`god`
|noclip|Toggles no-clip mode. (passing through map clipping).|`noclip`
|notarget|Toggles bots targeting your client.|`notarget`
|players|Show currently connected players and their status.|`players`
|score|Request score-data from the server.|`score`
|team|Moves your client into a team.|`team <a/s/f/b/r>` (note: A=any team, S=spectator, F=free team, B=blue team, R=red team)
|vote|Casts a vote from your client.|`vote <yes/no/1/2/3>` (note: 1/2/3=map 1/2/3 on end-game voting)
|userinfo|Sends user-info to the server.|`userinfo <user-info data (\\ delimited)>`









------------------------
This list is still under development and is not complete or guaranteed to be accurate.
