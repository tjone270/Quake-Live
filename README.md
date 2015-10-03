# Quake Live DS - Scripts
Useful scripts for configuring the Quake Live Dedicated Server.

QuakeStart.sh:
This script is a big extension to the one supplied with the documentation. It is not intended to be run as-is, you must edit it to suit your environment. It will create multiple servers based off of argument 1, parsed by supervisor to the script. As I've had trouble with map-pool files, each server has it's own map-pool, which also defines it's game type, which is named mappool.txt as the server runs, until that file is overwritten by the next server and it's map-pool.

QuakeUpdate.sh:
This script is designed to be crowned, I have mine running every day at 8:00am GMT+10. It warns players connected to the servers that the servers will be going down for updates, stops all servers with supervisorctl, runs the steamcmd.sh update command, replaces the steam-deployed access.txt, workshop.txt and server.cfg files with pre-made backups, as sometimes these files are replaced during an update, and restarts the servers. Restarting the processes isn't necessary, but I've observed strange behaviour from the server if it starts to gain uptime over 3-4 days, so I restart them as a refresh.

AutoDownload.sh:
Occasionally, the workshop download function that's supposed to run upon server start doesn't function properly. This script will manually download every workshop item listed in your workshop.txt directory, and move it into the qlds/steamapps/workshop directory. After you restart your server, the workshop items will become available.

SearchLogs.sh:
This script allows you to find specific log entries from any of the log files in /tmp. Example of use:
./searchlogs.sh "some sort of error" 0 3
The 0 is the server ID, so the server running as qzeroded_0 is ID 0. 
The 3 is the number of surrounding lines to include, so if the script finds a line containing the string, the 3 will tell it to print 3 lines above and below that line, to provide extra info/context.
