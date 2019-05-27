# mSort

## Version Info
  * python 3.7.3
  * keyboard 0.13.3
  * pip 19.1.1
  * pygame 1.9.6
  * mutagen 1.42.0

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

Remove unncessary 'global' tags in functions. seems like they are only needed for variables that appear on the left side of an assignment statemtnt. possibly only before they are used on the right side. possibly not.

add some kind of search feature. this is probably going to be a process: some hotkey combo to start up a search -> some way to cancel or speech recognition or take over the keyboard and consume everything until enter -> use some kind of predictive text/spellcheck/injection engine to figure out what the user actually wants -> find it in the list, set the songnum, and hit play. if it finds more than one thing it might try using google text to speech to list out the options and let you press a number button, one through zero, say to select one.

add more analytics stuff. tracking a song's plays perhaps (all the way through)

possibly add some way to 'like' a song. perhaps a hotkey and a new metadata int. only once per play?

get the metadata, settings, etc. to sync.

figure out how to use the metadata

put some way to mark songs as damaged and wheneger a song throws an error message mark it as damaged and move on. conveniently we have some damaged songs to use as guinnea pigs. songs that are marked as damaged should immediately be removed from metadata and instead written to a text doc. any songs that are on 'damaged.txt' should not have any new metadata tracked for them. when a song is removed from 'damaged.txt' metadata should start being collected for it again immediately. the idea here is that the user should check this list, remove all of those songs, and remove 'broken.txt'. then the user can fix and put back any number of the afflicted songs. if a song is marked broken on accident or without good cause there is little harm. just leave the song and remove 'broken.txt' or the entry therein. this will lead to some proportion issues with the metadata where it looks like a brand new song to the playlist when this happens. alternatively i could just let the metadata file bloat (allow it to keep collecting data and not remove entries for damaged songs). i think that might be a worse idea however.

have songs fade in and out

find some way to trim off the empty noise at the beginnings and ends of songs

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
