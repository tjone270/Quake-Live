#! /bin/bash
# quakestart.sh - quake live multiple server update script, utilising steamcmd.
# created by Thomas Jones on 09/09/15.
# purger@tomtecsolutions.com

# Defining variables:
export qBaseURL="https://raw.githubusercontent.com/tjone270/QuakeLiveDS_Scripts/master"
export qUpdateServerMessage="^7All ^4TomTec Solutions^7 hosted servers are going down ^1within a minute^7 for daily updating. They will be back in ^410 minutes^7."
export qUpdateLowestRconPort=28960
export qUpdateHighestRconPort=28970
export qRconPassword=$(<localConfig-rconPassword-purgery.txt)

echo "========== QuakeUpdate.sh has started. =========="
echo "========= $(date) ========="
# Informing players in the servers that the servers are going down for a bit.
counter="$qUpdateLowestRconPort"

while [ $counter -le $qUpdateHighestRconPort ]
do
	echo Telling players in server port $counter that the servers are going down...
	python2 ~/steamcmd/steamapps/common/qlds/rcon.py --host tcp://127.0.0.1:$counter --password "$qRconPassword" --command "say $qUpdateServerMessage"
	((counter++))
done

# Using 'supervisorctl' to stop all servers.
echo Stopping Quake Servers...
/usr/local/bin/supervisorctl stop all

# Running 'steamcmd' to update qzeroded
echo Updating Quake Server...
~/steamcmd/steamcmd.sh +login anonymous +force_install_dir ~/steamcmd/steamapps/common/qlds/ +app_update 349090 +quit

# Updating mappools/configs/factories
curl $qBaseURL/scripts/quakeconfig.sh > quakeconfig.sh; dos2unix quakeconfig.sh; chmod +x quakeconfig.sh
sh quakeconfig.sh

# Removing the .quakelive directories, except for baseq3.
echo Removing Purgery port directories...
cd ~/.quakelive
rm -rf 27960 27961 27962 27963 27964 27965 27966 27967 27968 27969 27970
cd ~

# Running 'autodownload.sh' to recache all workshop items before restarting.
bash ~/autodownload.sh

# Using 'supervisorctl' to start all servers.
echo Starting Quake Servers...
/usr/local/bin/supervisorctl start all

# Pretty obvious what's happening now.
echo Exiting...
exit 0
