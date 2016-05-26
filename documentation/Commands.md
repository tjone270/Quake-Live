# Quake Live Documentation

## Commands (regular)
| Command | Description | Syntax | Client | Server |
| :------ | :---------: | ------ | :----: | :----: |
|aclear
|alias
|arena
|astatus
|-attack
|+attack
|-back
|+back
|bind
|bindlist
|-button2
|+button2
|-button3
|+button3
|centerview|Centers the vertical view pitch of the player.|`centerview`|:white_check_mark:|:x:|
|changeVectors
|clear|Clear the console scrollback.|`clear`|:white_check_mark:|:x:|
|clearcvar|Clears the specified CVAR's value, setting it to Null ("")|`clearcvar <cvar>`|:white_check_mark:|:white_check_mark:|
|clientfriendinvite
|clientinfo
|clientkick|Kicks a player/bot by client ID|`clientkick <client id>`|:white_check_mark:|:white_check_mark:
|clientviewprofile
|cmd
|cmdlist|Alias of `listcmds`|
|condump
|configstrings
|connect
|connect_lobby
|cvarAdd|Adds/subtracts an int/float stored in a CVAR.|Add:`cvaradd s_volume +0.05`  Subtract:`cvaradd s_volume -0.05`|:white_check_mark:|:white_check_mark:
|cvarlist|Alias of `listcvars`|
|cvarMult|Multiplies an int/float stored in a CVAR.|`cvarmult s_volume 5`|:white_check_mark:|:white_check_mark:
|cvar_restart|Restarts the CVAR subsystem. Note that this clears most changes to CVARs.|`cvar_restart`|:white_check_mark:|:white_check_mark:|
|demo
|devmap|Loads a map in development/cheats mode. Will append a `cheats` tag to your server while in devmap mode.|`devmap <map> [factory]`|:white_check_mark:|:white_check_mark:|
|dir
|disconnect|Disconnect from the current server.|`disconnect`|:white_check_mark:|:x:|
|dumpuser|Prints the player's `userinfo` to the console.|`dumpuser <player name>`
|echo
|exec|Executes a configuration file.|`exec <config file>`|:white_check_mark:|:white_check_mark:|
|fdir
|find
|-forward
|+forward
|fs_openedList
|fs_referencedList
|gfxinfo
|imagelist
|in_restart|Restarts the game input subsystem.|`in_restart`|:white_check_mark:|:x:
|kick|Kick a player by name.|`kick <player name>`|:white_check_mark:|:white_check_mark:|
|killserver|Unload the currently loaded map and put the server in a 'map-less' state (does not exit the process but shuts down the game, further `map` commands can be run to recover the server)|`killserver`|:white_check_mark:|:white_check_mark:
|-left
|+left
|listcmds|Lists all commands with optional filtering.|`listcmds [filter]`|:white_check_mark:|:white_check_mark:
|listcvars|Lists all CVARs with optional filtering.|`listcvars [filter]`|:white_check_mark:|:white_check_mark:
|ListInputDevices|Lists all input devices.|`listinputdevices`|:white_check_mark:|:x:
|-lookdown
|+lookdown
|-lookup
|+lookup
|map|Loads a map normally.|`map <map name> [factory]`|:white_check_mark:|:white_check_mark:|
|map_restart|Reloads the map, it's entities and respawns all players.|`map_restart`|
|meminfo|Shows memory allocation information.|`meminfo`|:white_check_mark:|:white_check_mark:|
|messagemode|Calls the `say` chat dialog.|`messagemode`|:white_check_mark:|:x:
|messagemode2|Calls the `say_team` chat dialog.|`messagemode`|:white_check_mark:|:x:
|midiinfo|Display MIDI device information.|`midiinfo`|:white_check_mark:|:x:
|-mlook
|+mlook
|model|Get/set the current player model/skin.|`model [model/skin]`|:white_check_mark:|:x:
|modelist|Display a list of monitor configurations that `r_mode` will accept.|`modelist`|:white_check_mark:|:x:
|modellist|A list of all model files currently loaded/in use.|`modellist`|:white_check_mark:|:x:
|-movedown
|+movedown
|-moveleft
|+moveleft
|-moveright
|+moveright
|-moveup
|+moveup
|music|Plays a looping music track in-game.|`music <path to music file> [loop file]`|:white_check_mark:|:x:
|net_restart|Restarts the networking subsystem.|`net_restart`|:white_check_mark:|:x:
|path|Show the current paths in the search path and whether or not those files are pure. Also show currently opened files (handles).|`path`|:white_check_mark:|:white_check_mark:
|play|Plays a sound in-game.|`play <path to sound file>`|:white_check_mark:|:x:
|postprocess_restart|Restarts the post-processing subsystem.|`postprocess_restart`|:white_check_mark:|:x:
|quit|Exits the client/server process immediately and shuts down the game.|`quit`|:white_check_mark:|:white_check_mark:|
|reconnect|Reconnect to the last server you were connected to. If you're connected to a server, it'll reconnect to your current server.|`reconnect`|:white_check_mark:|:x:
|record|Records a demo in-game.|`record <file name>`|:white_check_mark:|:x:
|reload_arenas|Reloads the arena definitions (`.arenas`)|`reload_arenas`|:white_check_mark:|:white_check_mark:|
|reload_factories|Reloads all the factories (will read in new factories) from pak00.pk3/scripts/factories.txt and scripts/*.factories|`reload_factories`|:white_check_mark:|:white_check_mark:|
|reload_mappool|Reloads the map-pool file specified in the `sv_mappoolFile` CVAR.|`reload_mappool`|:white_check_mark:|:white_check_mark:|
|reset|Resets a CVAR to it's initial value.|`reset <cvar>`|:white_check_mark:|:white_check_mark:|
|-right
|+right
|say|Send a message from the client/server. Server messages are prefixed with `Server: `, client messages are prefixed with `PlayerName: ^2 `|`say <message>`|:white_check_mark:|:white_check_mark:
|screenshot|Write a screenshot in TGA format.|`screenshot [file name]`|:white_check_mark:|:x:
|screenshotJPEG|Write a screenshot in JPEG format.|`screenshotjpeg [file name]`|:white_check_mark:|:x:
|sectorlist|List the map's sectors and the number of entities within the sectors.|`sectorlist`|:white_check_mark:|:x:
|serverinfo|Displays all CVARs with flag 64 set. These CVARs can be queried via the Valve source protocol from the server's `net_port`.|`serverinfo`|:white_check_mark:|:white_check_mark:|
|set|Sets a CVAR with no special flags set.|`set <cvar> <value>`|:white_check_mark:|:white_check_mark:|
|seta|Sets a CVAR with the archive flag set.|`seta <cvar> <value>`|:white_check_mark:|:white_check_mark:|
|setenv
|shaderlist
|showip|Display current IP address(es).|`showip`|:white_check_mark:|:x:
|s_info|Display sound/audio system information.|`s_info`|:white_check_mark:|:x:
|skinlist|List loaded 'skins' for the currently selected player model.|`skinlist`|:white_check_mark:|:x:
|s_list|List all currently loaded/buffered sound files.|`s_list`|:white_check_mark:|:x:
|snd_restart|Restarts the audio subsystem.|`snd_restart`|:white_check_mark:|:x:
|-speed
|+speed
|s_stop|Stop playing the looping music track.|`s_stop`|:white_check_mark:|:x:
|startRandomMap|Runs a random map listed in the map-pool file (with the factory also specified). By default this runs on server startup unless specified otherwise.|`startRandomMap`|:white_check_mark:|:white_check_mark:|
|status|List all clients, and their Client IDs, scores, latency in milliseconds (ping), in-game name, lastmsg, IP address, QPort, player rate and Steam64 ID.|`status`|:white_check_mark:|:white_check_mark:|
|steam_downloadugc
|steam_subscribeugc
|steam_unsubscribeugc
|stoprecord|Stops recording a demo.|`stoprecord`|:white_check_mark:|:x:
|-strafe
|+strafe
|toggle
|toggleconsole
|touchFile
|unalias
|unaliasall
|unbind
|unbindall
|userinfo
|vid_restart|Restarts the graphics subsystem.|`vid_restart`|:white_check_mark:|:x:
|-voice
|+voice
|vstr
|wait
|web_changeHash
|web_clearCache
|web_hideBrowser
|web_reload|For development use only. Will trap your client in the old Quake 3 Arena menu system, requires a relaunch to get back to normal functionality|`web_reload`|:white_check_mark:|:x:
|web_showBrowser
|web_showError
|writeClientConfig
|writeconfig


------------------------
This list is still under development and is not complete or guaranteed to be accurate.
