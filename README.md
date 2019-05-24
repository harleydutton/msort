##mSort

#Version Info
	* python 3.7.3
	* keyboard 0.13.3
	* pip 19.1.1
	* pygame 1.9.6

#Description
mSort is a custom media player I have written in python to include some custom features I was not able to find in commercially available media players.

#Common features (to be) included
	* having hotkeys for common actions: play/pause,prev,next,and volume
	* shuffle mode
	* some way to specify a music folder
	* persistient settings such as volume and where to find music

#Custom features
	* creating, tracking, and syncing many bits of metadata for each song including
		** times skipped (hitting the 'previous' will skips)
		** times played (all the way through)
		** volume changes at various points in a song
	* a hotkey to mark a song as damaged
	* global hooks to listen to keyboard when not focused
	
#Devlopment Log

Encountered many problems with python. switching to java. should help with android port.
Java is worse. switching back.
Back to python. Read the pygame documentation and got everything working. RTFM I guess.
Working on creating/tracking metadata now. Also, getting the volume to be persistient.