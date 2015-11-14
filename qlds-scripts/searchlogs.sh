#! /bin/bash
# searchlogs.sh - quake live dedicated server log view utility.
# created by Thomas Jones on 02/10/15.
# purger@tomtecsolutions.com

if [ $# -eq 0 ]; then
    echo "Usage:"
    echo "    ./searchlogs.sh <string> <server id> <surrounding lines>"
    echo ""
    echo "Example:"
    echo "    ./searchlogs.sh 'tjone270' 0 3"
    exit 1
fi

echo "Searching for '$1' on server \#$2..."
sudo grep -niC $3 "$1" /tmp/qzeroded_$2* | more -d
echo Done.
exit 0

