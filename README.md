# Quake Live Dedicated Server

## Autonomous Server System, in Bash Script.

_if you're looking for the standalone scripts, that don't use quakeconfig.sh, [click here](https://github.com/tjone270/QuakeLiveDS_Scripts/releases/tag/v1.0)._

The scripts/mappools/factories/configs here are currently live on The Purgery servers hosted in Australia. (they're downloaded every day at 8:00am GMT+10, so if something changes here on GitHub, it'll be live on the servers within 24 hours.)

To use these scripts, you'll need to clone this repository and point the _quakeconfig.sh_ script to it, or simply remove _quakeconfig.sh_ from the _quakeupdate.sh_ script and manually edit the files yourself. 

The downside to doing that, is not having a central location to pull the new scripts/updated files, and having it replicate across more than one server. Also, Steam will over-write some files occasionally, it depends on whether a developer has modified any file, if so, it'll be overwritten. That doesn't happen if _quakeconfig.sh_ is being used.
