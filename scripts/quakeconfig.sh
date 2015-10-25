#! /bin/bash
# quakeconfig.txt - quake live server file sync.
# created by Thomas Jones on 09/10/15.
# purger@tomtecsolutions.com

echo "========== QuakeConfig.sh has started. =========="
echo "========= $(date) ========="

# Variables used in multiple scripts:
cd ~
export qBaseURL="https://raw.githubusercontent.com/tjone270/QuakeLiveDS_Scripts/master"
#export qRconPassword=$(<localConfig-rconPassword.txt)
#export qSteamUsername=$(<localConfig-steamUsername.txt)
#export qSteamPassword=$(<localConfig-steamPassword.txt)
#export qServerLocation=$(<localConfig-serverLocation.txt)
#export qUpdateServerMessage="^4The Purgery^7 servers are going down ^4within a minute^7 for daily updating. They will be back in ^410 minutes^7."
#export qUpdateLowestRconPort=28960
#export qUpdateHighestRconPort=28970
export qPathToStartScript="~/steamcmd/steamapps/common/qlds/run_server_x64.sh"
export qStartPathToBaseQ3="~/steamcmd/steamapps/common/qlds/baseq3"
export qQLDSpath="~/steamcmd/steamapps/common/qlds"

# Downloading a new copy of some files.
echo "Downloading and replacing 'quakestart.sh'..."
rm quakestart.sh; curl -s $qBaseURL/scripts/quakestart.sh > quakestart.sh; dos2unix --quiet quakestart.sh; chmod +x quakestart.sh
echo "Downloading and replacing 'quakeupdate.sh'..."
rm quakeupdate.sh; curl -s $qBaseURL/scripts/quakeupdate.sh > quakeupdate.sh; dos2unix --quiet quakeupdate.sh; chmod +x quakeupdate.sh
echo "Downloading and replacing 'autodownload.sh'..."
rm autodownload.sh; curl -s $qBaseURL/scripts/autodownload.sh > autodownload.sh; dos2unix --quiet autodownload.sh; chmod +x autodownload.sh
echo "Stopping, downloading and replacing 'quakemotd.sh'..."
killall quakemotd.sh; rm quakemotd.sh; curl -s $qBaseURL/scripts/quakemotd.sh > quakemotd.sh; dos2unix --quiet quakemotd.sh; chmod +x quakemotd.sh;
# RCON occasionally breaks the server, so this shouldn't be used until I find a solution.
#echo "Starting 'quakemotd.sh'..."
# ./quakemotd.sh &
cd ~/steamcmd/steamapps/common/qlds/baseq3
echo "Downloading and replacing 'baseq3\server.cfg'..."
rm server.cfg; curl -s $qBaseURL/config-files/server.txt > server.cfg; dos2unix --quiet server.cfg
# No need to run this anymore, as there are now more than one access file.
#  echo "Downloading and replacing 'baseq3\access.txt'..."
#  rm access.txt; curl -s $qBaseURL/config-files/access.txt > access.txt; dos2unix --quiet access.txt
echo "Downloading and replacing 'baseq3\workshop.txt'..."
rm workshop.txt; curl -s $qBaseURL/config-files/workshop.txt > workshop.txt; dos2unix --quiet workshop.txt
echo "Downloading and updating all access files..."
rm -f access*; curl -s $qBaseURL/accesses/accesses.zip > accesses.zip; unzip -o accesses.zip; rm accesses.zip; rm -rf __MACOSX; dos2unix --quiet access*
echo "Downloading and updating all map-pool files..."
rm -f mappool_*; curl -s $qBaseURL/mappools/mappools.zip > mappools.zip; unzip -o mappools.zip; rm mappools.zip; rm -rf __MACOSX; dos2unix --quiet mappool_*
echo "Downloading and updating all factories..."
rm -rf scripts/; curl -s $qBaseURL/factories/factories.zip > factories.zip; unzip -o factories.zip; rm factories.zip; rm -rf __MACOSX; mkdir scripts; mv *.factories scripts/; dos2unix --quiet scripts/*
echo "Downloading and replacing all entities..."
rm -rf entities/; curl -s $qBaseURL/entities/entities.zip > entities.zip; unzip -o entities.zip; rm entities.zip; rm -rf __MACOSX; mkdir entities; mv *.ent entities/; dos2unix --quiet entities/*
echo "Downloading and replacing '/etc/supervisord.conf'..."
sudo rm /etc/supervisord.conf; curl -s $qBaseURL/config-files/supervisord.txt > supervisord.conf; sudo mv supervisord.conf /etc/supervisord.conf; sudo dos2unix --quiet /etc/supervisord.conf; sudo chmod 755 /etc/supervisord.conf
echo Done.
# Updating this script. THIS IS NOW TAKEN CARE OF IN THE UPDATE SCRIPT
#  cd ~
#  curl -s $qBaseURL/scripts/quakeconfig.sh > quakeconfig.sh; dos2unix --quiet quakeconfig.sh; chmod +x quakeconfig.sh

# Finished.
exit 0