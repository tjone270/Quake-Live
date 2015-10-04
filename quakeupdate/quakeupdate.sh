#! /bin/bash
# quakestart.sh - quake live multiple server update script, utilising steamcmd.
# created by Thomas Jones on 09/09/15.
# purger@tomtecsolutions.com

# Defining variables.
steamUser=""
steamPass=""
rconPass=""
highestPort=28969
message="^4The Purgery^7 servers are going down ^4within a minute^7 for daily updating. They will be back in ^410 minutes^7."

echo "========== QuakeUpdate.sh has started. =========="
# Informing players in the servers that the servers are going down for a bit.
counter=28960
while [ $counter -le $highestPort ]
do
	echo Telling players in server port $counter that the servers are going down...
	/home/qlserver/steamcmd/steamapps/common/qlds/rcon.py --host tcp://127.0.0.1:$counter --password "$rconPass" --command "say $message"
	((counter++))
done

# Using 'supervisorctl' to stop all servers.
echo Stopping Quake Servers...
/usr/local/bin/supervisorctl stop all

# Running 'steamcmd' to update qzeroded
echo Updating Quake Server...
/home/qlserver/steamcmd/steamcmd.sh +login "$steamUser" "$steamPass" +force_install_dir /home/qlserver/steamcmd/steamapps/common/qlds/ +app_update 349090 +quit

# Replacing the steam configuration, which so politely replaces my 
# nice configuration for it's one, primarily for 'com_hunkmegs 60' reasons.
echo Replacing new config. with old good config, and backing up new config.
mv -fv /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/server.cfg /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/server.bak 
cp -Rfv /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/goodserver.cfg /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/server.cfg

# Replacing the steam-deployed access file, which so politely replaces my 
# nice access file for it's one.
echo Replacing new access file. with old good access file, and backing up new access file.
mv -fv /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/access.txt /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/access.bak 
cp -Rfv /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/goodaccess.txt /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/access.txt

# Replacing the steam-deployed workshop file, which so politely replaces my
# nice workshop file for it's one.
echo Replacing new workshop file. with old good workshop file, and backing up new workshop file.
mv -fv /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/workshop.txt /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/workshop.bak
cp -Rfv /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/goodworkshop.txt /home/qlserver/steamcmd/steamapps/common/qlds/baseq3/workshop.txt

# Removing the .quakelive directories, except for baseq3.
echo Removing 2* directories...
rm -rf /home/qlserver/.quakelive/2*

# Running 'autodownload.sh' to recache all workshop items before restarting.
bash /home/qlserver/autodownload.sh

# Using 'supervisorctl' to start all servers.
echo Starting Quake Servers...
/usr/local/bin/supervisorctl start all

# Pretty obvious what's happening now.
echo Exiting...
exit 0
