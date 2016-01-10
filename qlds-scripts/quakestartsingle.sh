#! /bin/bash
# quakestartsingle.sh - quake live single server spawning script.
# created by Thomas Jones on 11/01/16.
# thomas@tomtecsolutions.com

export qPathToStartScript="~/steamcmd/steamapps/common/qlds/run_server_x64.sh"

gameport=`expr $1 + 27960`
rconport=`expr $1 + 28960`

echo "========== QuakeStart.sh has started. =========="
echo "========= $(date) ========="
cd ~/steamcmd/steamapps/common/qlds/baseq3

exec $qPathToStartScript \
    +set net_strict 1 \
    +set net_port $gameport \
    +set sv_hostname "My Quake Server Name" \
    +set zmq_rcon_enable 1 \
    +set zmq_rcon_password "password" \
    +set zmq_rcon_port $rconport \
    +set zmq_stats_enable 1 \
    +set zmq_stats_password "password" \
    +set zmq_stats_port $gameport \
    +set sv_tags "My Server Tag, My Server Location" \
    +set g_voteFlags "0" \
    +set g_accessFile "access.txt" \
    +set sv_mappoolFile "mappool.txt" \
    +set fs_homepath ~/.quakelive/$gameport
