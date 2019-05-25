# mSort

## Version Info
  * python 3.7.3
  * keyboard 0.13.3
  * pip 19.1.1
  * pygame 1.9.6

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
At some point I need to check the songs loaded from metadata against the songs in the playlist. Then maybe remove them? maybe give up on syncing? If i remove them then sync that seems like a great way to lose all my metadata (assuming something went wrong and it didn't load the list of songs for some reason). Maybe keep a separate, easily deletable list of damaged songs and assume the user will remove them from rotation. Remove and do not track metadata for any songs on this list. Seems like a viable solution.

Remove unncessary 'global' tags in functions. seems like they are only needed for variables that appear on the left side of an assignment statemtnt. possibly only before they are used on the right side. possibly not.

Fix whatever is causing some songs to play too slowly. I am guessing this is a bitrate issue and can be fixed by standardizing that. 'sampling' might be a handy keyword in SOS searches.

add some kind of search feature. this is probably going to be a process: some hotkey combo to start up a search -> some way to cancel or speech recognition or take over the keyboard and consume everything until enter -> use some kind of predictive text/spellcheck/injection engine to figure out what the user actually wants -> find it in the list, set the songnum, and hit play. if it finds more than one thing it might try using google text to speech to list out the options and let you press a number button, one through zero, say to select one.

add more analytics stuff.

get the metadata, settings, etc. to sync.

figure out how to use the metadata

## Devlopment Log
Encountered many problems with python. switching to java. should help with android port.
Java is worse. switching back.
Back to python. Read the pygame documentation and got everything working. RTFM I guess.
Working on creating/tracking metadata now. Also, getting the volume to be persistient.
Updated README.md. Should be up to code now.
I don't seem to need 'global' for some function variables. Need to go through and remove the extras.
Adding metadata tracking and whatnot. Skips and 'unskips' right now. soon: the world.
okay cool we have it tracking skips and unskips. it might also be saving the volume. i didnt check.
