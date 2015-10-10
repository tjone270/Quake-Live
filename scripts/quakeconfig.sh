#! /bin/bash
# quakeconfig.txt - quake live server file sync.
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
export qQLDSpath="~/steamcmd/steamapps/common/qlds"

# Downloading a new copy of some files.
rm quakestart.sh; curl $qBaseURL/scripts/quakestart.sh > quakestart.sh; dos2unix quakestart.sh; chmod +x quakestart.sh
rm quakeupdate.sh; curl $qBaseURL/scripts/quakeupdate.sh > quakeupdate.sh; dos2unix quakeupdate.sh; chmod +x quakeupdate.sh
cd ~/steamcmd/steamapps/common/qlds/baseq3
rm server.cfg; curl $qBaseURL/config-files/server.txt > server.cfg; dos2unix server.cfg
rm access.txt; curl $qBaseURL/config-files/access.txt > access.txt; dos2unix access.txt
rm workshop.txt; curl $qBaseURL/config-files/workshop.txt > workshop.txt; dos2unix workshop.txt
rm -f mappool_*; curl $qBaseURL/mappools/mappools.zip > mappools.zip; unzip -o mappools.zip; rm mappools.zip; rm -rf __MACOSX; dos2unix mappool_*
rm -rf scripts/; curl $qBaseURL/factories/factories.zip > factories.zip; unzip -o factories.zip; rm factories.zip; rm -rf __MACOSX; mkdir scripts; mv *.factories scripts/; dos2unix scripts/*
rm -rf entities/; curl $qBaseURL/entities/entities.zip > entities.zip; unzip -o entities.zip; rm entities.zip; rm -rf __MACOSX; mkdir entities; mv *.ent entities/; dos2unix entities/*
sudo rm /etc/supervisord.conf; curl $qBaseURL/config-files/supervisord.txt > supervisord.conf; sudo mv supervisord.conf /etc/supervisord.conf; sudo dos2unix /etc/supervisord.conf; sudo chmod 755 /etc/supervisord.conf

# Updating this script.
cd ~
curl $qBaseURL/scripts/quakeconfig.sh > quakeconfig.sh; dos2unix quakeconfig.sh; chmod +x quakeconfig.sh

# Finished.
exit 0