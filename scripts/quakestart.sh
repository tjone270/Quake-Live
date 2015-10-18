#! /bin/bash
# quakestart.sh - quake live multiple server spawning script.
# created by Thomas Jones on 09/09/15.
# purger@tomtecsolutions.com


# Defining variables.
export qServerLocation=$(<localConfig-serverLocation.txt)
export qPathToStartScript="~/steamcmd/steamapps/common/qlds/run_server_x64.sh"
export qRconPassword=$(<localConfig-rconPassword.txt)

sponsortag="$qServerLocation, TomTec Solutions"

gameport=`expr $1 + 27960`
rconport=`expr $1 + 28960`
servernum=`expr $1 + 0`

# Executing a random delay to stagger the spawning of each server, as
# supervisord starts everything at once, thus lowering the load surge.
#	echo "Sleeping for random delay (5-30 seconds) before spawning..."
#	sleep $(((RANDOM%120)+10))
# No-one cares about this anymore, sleeping on a per-server basis now?
# Finally works, should mean that all servers should be up after 45 seconds.

# Starts servers with different settings, based off the process number parsed
# as argument 1 by supervisord. 

echo "========== QuakeStart.sh has started. =========="
echo "========= $(date) ========="
#echo "arg1 is equal to $1"
cd ~/steamcmd/steamapps/common/qlds/baseq3

if [ $1 -le 1 ]
# starting PQL CA 1 and 2...
then
echo "Starting clan arena server 1 or 2..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "   #$servernum The Purgery $qServerLocation PQL - Clan Arena" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
	+set bot_enable 1 \
	+set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_pqlca.txt" \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 2 ]
# starting PQL Race 1...
then
echo "Starting race server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $qServerLocation PQL - Race" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "grappling hook, crouch slide, $sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_pqlrace.txt" \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 3 ]
# starting PQL FFA 1...
then
echo "Starting free for all server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $qServerLocation PQL - Free For All (Beta)" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_pqlffa.txt" \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 4 ]
# starting PQL CTF 1...
then
echo "Starting capture the flag server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $qServerLocation PQL - Capture the Flag" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_pqlctf.txt" \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 5 ]
# starting PQL DOM 1...
then
echo "Starting domination server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $qServerLocation PQL - Domination" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_pqldom.txt" \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 6 ]
# starting PQL INFECTED 1...
then
echo "Starting infected server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $qServerLocation PQL - Infected (Beta)" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "zombies, $sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_pqlinfected.txt" \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 7 ]
# starting PQL TDM 1...
then
echo "Starting team deathmatch server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $qServerLocation PQL - Team Deathmatch (Beta)" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_pqltdm.txt" \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 8 ]
# starting PQL MultiGame 1...
then
echo "Starting multi game type server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $qServerLocation PQL - Multi-Gametype Turbo (Beta)" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_allowSpecVote 1 \
    +set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
    +set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_pqlmulti.txt" \
    +set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 9 ]
# starting vql duel 1...
then
echo "Starting VQL duel server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $qServerLocation VQL - Duel" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
    +set g_allowSpecVote 1 \
    +set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
    +set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_vqlduel.txt" \
    +set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 10 ]
# starting VQL iCTF 1...
then
echo "Starting VQL iCTF type server 1..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname " #$servernum The Purgery $qServerLocation VQL - iCTF" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$qRconPassword" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$qRconPassword" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_allowSpecVote 1 \
    +set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
    +set bot_nochat 1 \
    +set g_accessFile "access_purgery.txt" \
    +set sv_mappoolFile "mappool_vqlictf.txt" \
    +set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 11 ]
# starting mickzerofive's brisbane server 1...
then
if [ $(hostname) == "brisbane.quakelive.tomtecsolutions.com.au" ]
then
echo "Starting mickzerofive's server..."
exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "http://4SeasonsGaming.com $qServerLocation" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "PASSWORD" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "PASSWORD" \
    +set zmq_stats_port $gameport \
    +set sv_tags "4Seasons Gaming, $qServerLocation" \
    +set g_allowSpecVote 1 \
    +set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
    +set bot_nochat 1 \
    +set g_accessFile "access_mickzerofive.txt" \
    +set sv_mappoolFile "mappool_default.txt" \
    +set fs_homepath ~/.quakelive/$gameport
else
echo "This system is not intended to host MickZeroFive's server."
fi

fi


# Unused cvars.
# +set sv_mapPoolFile "mappool_pqlca.txt" \
# +set net_ip "quakelive.tomtecsolutions.com.au" \
# +set com_hunkMegs 30 \
# +set sv_idleExit 0