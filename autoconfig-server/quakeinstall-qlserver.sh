#! /bin/bash
# quakeinstall-qlserver.sh - quake live dedicated server installation for qlserver user.
# intended to be run on a fresh VPS/Dedicated Server, this script must be run under the qlserver user.
# created by Thomas Jones on 29/09/15.

steamUser=""
steamPass=""

if [ "$(whoami)" -ne "qlserver" ]
  then echo "Please run under user 'qlserver'."
  exit
fi
clear
echo "Installing SteamCMD..."
mkdir ~/steamcmd; cd ~/steamcmd; wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz; tar -xvzf steamcmd_linux.tar.gz; rm steamcmd_linux.tar.gz
clear
echo "Installing Quake Live Dedicated Server..."
./steamcmd.sh +login "$steamUser" "$steamPass" +force_install_dir /home/qlserver/steamcmd/steamapps/common/qlds/ +app_update 349090 +quit
clear
echo "Cronning 'QuakeUpdate.sh'..."
echo "0 4 * * * /home/qlserver/quakeupdate.sh" > cron; crontab cron; rm cron
clear
echo "Done."
exit