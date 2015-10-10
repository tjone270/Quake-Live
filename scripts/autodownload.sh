#! /bin/bash
# autodownload.sh - quake live dedicated server workshop item download utility.
# created by Thomas Jones on 03/10/15.
# purger@tomtecsolutions.com

echo "========== AutoDownload.sh has started. =========="
echo "========== $(date) =========="

BLUE="\033[0;34m"
NC="\033[0m"
workshopIDs=`cat ~/steamcmd/steamapps/common/qlds/baseq3/workshop.txt | grep -v '#' | sed '/^[ \t]*$/d'`
numOfIDs=`echo "$workshopIDs" | wc -l`
counter=0
while [ $counter -lt $numOfIDs ]; do
	currentID=`echo $workshopIDs | awk '{ print $1 }'`
	workshopIDs=`echo $workshopIDs | cut -d ' ' -f2-`
	echo -e "\n\n${BLUE}Downloading item $currentID from Steam... ($counter/$numOfIDs)${NC}\n"
	~/steamcmd/steamcmd.sh +login anonymous +workshop_download_item 344320 $currentID +quit > /dev/null
	((counter++))
done
echo -e "\n\n${BLUE}Removing old workshop data and moving new items into place...${NC}"
rm -r ~/steamcmd/steamapps/common/qlds/steamapps/workshop
mv ~/steamcmd/steamapps/workshop/ ~/steamcmd/steamapps/common/qlds/steamapps/workshop
echo Done.
exit 0