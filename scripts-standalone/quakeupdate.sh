#! /bin/bash
# quakestart.sh - quake live multiple server update script, utilising steamcmd.
# created by Thomas Jones on 09/09/15.
# thomas@tomtecsolutions.com

echo "========== QuakeUpdate.sh has started. =========="
echo "========= $(date) ========="

# Using 'supervisorctl' to stop all servers.
echo Stopping Quake Servers...
/usr/local/bin/supervisorctl stop all

# Running 'steamcmd' to update qzeroded
echo Updating Quake Server...
~/steamcmd/steamcmd.sh +login anonymous +force_install_dir ~/steamcmd/steamapps/common/qlds/ +app_update 349090 +quit

# Running 'autodownload.sh' to recache all workshop items before restarting.
echo Updating Steam workshop items...
bash ~/autodownload.sh

# Using 'supervisorctl' to start all servers.
echo Starting Quake Servers...
/usr/local/bin/supervisorctl start all

# Pretty obvious what's happening now.
echo Exiting...
exit 0
