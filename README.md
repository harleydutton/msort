# mSort

## Version Info
  * python 3.7.3
  * keyboard 0.13.3
  * pip 19.1.1
  * pygame 1.9.6
  * mutagen 1.42.0
  * fuzzywuzzy 0.17.0

## Description
mSort is a custom media player I have written in python to include some custom features I was not able to find in commercially available media players.

## Common features (to be) included
  * having hotkeys for common actions: play/pause,prev,next,and volume
  * shuffle mode
  * some way to specify a music folder
  * persistient settings such as volume and where to find music
  * notably this app has no GUI and so cannot cherry-pick songs to play off a list

## Custom features
  * a hotkey to mark a song as damaged
  * global hooks to listen to keyboard when not focused
  * creating, tracking, and syncing many bits of metadata for each song including
    * times played (all the way through)
    * times skipped (-1 for hitting previous)
    * volume changes at various points in a song
    * damaged status (how/when will i remove this flag?)

## To Do
Track how many times a song has played all the way through.
when you skip() set the plays to -1 to counteract the default +1 if the song had no previous play count.

Add a way to like a song.
This should have a hotkey associated with it. perhaps the up arrow? track this with an int metadata or some such. seems like a good idea to limit this to once per play.

Syncing.
I am not sure what all I will want to sync. probably the metadata and damaged songs list. either don't track settings or only track global settings.

Have songs fade in and out.
I might need to go look for a new audio library. I am not sure pygame can handle this.

Find some way to remove silence at the beginning and ends of songs.
I saw something to this effect. let me provide a link. https://www.swharden.com/wp/2009-06-19-reading-pcm-audio-with-python/

automatic equalization

make a settings, filemanager, and IO module

remove unnecessary imports and modules. update readme with this info

track search accuracy

make mark-broken request a reason

make failed searches (based on a threshhold for the usual search accuracy) download songs from the internet

add some method for detecting online status

get transcription to work offline. this probably means finding a new library for the task

## Devlopment Log
Encountered many problems with python. switching to java. should help with android port.
Java is worse. switching back.
Back to python. Read the pygame documentation and got everything working. RTFM I guess.
Working on creating/tracking metadata now. Also, getting the volume to be persistient.
Updated README.md. Should be up to code now.
I don't seem to need 'global' for some function variables. Need to go through and remove the extras.
Adding metadata tracking and whatnot. Skips and 'unskips' right now. soon: the world.
okay cool we have it tracking skips and unskips. it might also be saving the volume. i didnt check.
added mutagen. this lets me check the sample rates of songs and reinit the mixer so they sound right.
made volume load and save properly. 
added mark broken and all that jazz
added search function. only works online.
