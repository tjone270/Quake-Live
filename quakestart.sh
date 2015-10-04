#! /bin/bash
# quakestart.sh - quake live multiple server spawning script.
# created by Thomas Jones on 09/09/15.
# purger@tomtecsolutions.com

# Defining variables.
pathToStartScript="/home/qlserver/steamcmd/steamapps/common/qlds/run_server_x64.sh"
pathToBaseQ3="/home/qlserver/steamcmd/steamapps/common/qlds/baseq3"

location=""
password=""
sponsortag="$location"

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
echo "========== $(date) =========="
#echo "arg1 is equal to $1"
cd $pathToBaseQ3

if [ $1 -le 1 ]
# starting PQL CA 1 and 2...
then
cp -f mappool_pqlca.txt mappool.txt
echo "Starting clan arena server 1 or 2..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $location PQL - Clan Arena" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
	+set bot_enable 1 \
	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 2 ]
# starting PQL Race 1...
then
sleep 5
cp -f mappool_pqlrace.txt mappool.txt
echo "Starting race server 1..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $location PQL - Race" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "grappling hook, crouch slide, $sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 3 ]
# starting PQL FFA 1...
then
sleep 10
cp -f mappool_pqlffa.txt mappool.txt
echo "Starting free for all server 1..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $location PQL - Free For All (Beta)" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 4 ]
# starting PQL CTF 1...
then
sleep 15
cp -f mappool_pqlctf.txt mappool.txt
echo "Starting capture the flag server 1..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $location PQL - Capture the Flag" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 5 ]
# starting PQL DOM 1...
then
sleep 20
cp -f mappool_pqldom.txt mappool.txt
echo "Starting domination server 1..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $location PQL - Domination" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 6 ]
# starting PQL INFECTED 1...
then
sleep 25
cp -f mappool_pqlinfected.txt mappool.txt
echo "Starting infected server 1..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $location PQL - Infected (Beta)" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "zombies, $sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 7 ]
# starting PQL TDM 1...
then
sleep 30
cp -f mappool_pqltdm.txt mappool.txt
echo "Starting team deathmatch server 1..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $location PQL - Team Deathmatch (Beta)" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 8 ]
# starting pql duel 1...
then
sleep 35
cp -f mappool_vqlduel.txt mappool.txt
echo "Starting PQL duel server 1..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "  #$servernum The Purgery $location VQL - Duel" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
    +set g_voteFlags "13320" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
elif [ $1 -eq 9 ]
# starting PQL MultiGame 1...
then
sleep 40
cp -f mappool_pqlmulti.txt mappool.txt
echo "Starting multi game type server 1..."
exec $pathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname " #$servernum The Purgery $location PQL - Multi-Gametype Turbo (Beta)" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "$password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "$password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "$sponsortag" \
	+set g_allowSpecVote 1 \
	+set g_allowVoteMidGame 1 \
    +set bot_enable 1 \
   	+set bot_nochat 1 \
	+set fs_homepath ~/.quakelive/$gameport
fi

# Unused cvars.
# +set sv_mapPoolFile "mappool_pqlca.txt" \
# +set net_ip "quakelive.tomtecsolutions.com.au" \
# +set com_hunkMegs 30 \
# +set sv_idleExit 0