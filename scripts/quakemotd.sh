#! /bin/bash
# quakemotd.sh - quake live message of the day server broadcaster.
# created by Thomas Jones on 10/10/15.
# purger@tomtecsolutions.com

# Defining variables:
export qRconPassword=$(<localConfig-rconPassword.txt)
export qMOTDcontent=$(<remoteConfig-motd.txt)
export qUpdateLowestRconPort=28960
export qUpdateHighestRconPort=28970
export qBaseURL="https://raw.githubusercontent.com/tjone270/QuakeLiveDS_Scripts/master"
export qDelayBetweenMOTDbroadcast="5"  # in seconds

# Broadcast MOTD to every server hosted locally.
counter="$qUpdateLowestRconPort"
while true
do
    while [ $counter -le $qUpdateHighestRconPort ]
    do
        echo "Broadcasting MOTD to port $counter"
        ~/steamcmd/steamapps/common/qlds/rcon.py --host tcp://127.0.0.1:$counter --password "$qRconPassword" --command "say \"$qMOTDcontent\""
        ((counter++))
    done

    # Reset counter.
    export counter="$qUpdateLowestRconPort"
    # Download latest MOTD from GitHub.
    curl $qBaseURL/motd.txt > remoteConfig-motd.txt; dos2unix remoteConfig-motd.txt

    sleep $qDelayBetweenMOTDbroadcast
done

exit 0