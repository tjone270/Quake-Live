#! /bin/bash
# quakeconfig.txt - quake live server variable configuration.
# created by Thomas Jones on 09/10/15.
# purger@tomtecsolutions.com


# Variables used in multiple scripts:
cd ~
export qBaseURL="https://raw.githubusercontent.com/tjone270/QuakeLiveDS_Scripts/master"
export qRconPassword=$(<localConfig-rconPassword.txt)
export qSteamUsername=$(<localConfig-steamUsername.txt)
export qSteamPassword=$(<localConfig-steamPassword.txt)
export qServerLocation=$(<localConfig-serverLocation.txt)
export qUpdateServerMessage="^4The Purgery^7 servers are going down ^4within a minute^7 for daily updating. They will be back in ^410 minutes^7."
export qUpdateLowestRconPort=28960
export qUpdateHighestRconPort=28970
export qPathToStartScript="~/steamcmd/steamapps/common/qlds/run_server_x64.sh"
export qStartPathToBaseQ3="~/steamcmd/steamapps/common/qlds/baseq3"
export qQLDSpath="/home/qlserver/steamcmd/steamapps/common/qlds/"

# Downloading a new copy of some files.
curl $qBaseURL/scripts/quakestart.sh > quakestart.sh
curl $qBaseURL/scripts/quakeupdate.sh > quakeupdate.sh
curl $qBaseURL/scripts/quakeconfig.sh > quakeconfig.sh
curl 