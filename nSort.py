import os
import json
import random

import pygame
import keyboard
import mutagen.mp3

import fileman
from search import search
from scribe import transcribe
from record import rec
from stopwatch import lap

######################################################################
######################################################################

#remaining questions
#can we prettify the json objects being sent to fileman
#can we write as csv for excel?

#the format for songs will be a list of (path,filename) tuples
#the format for broken will be a dictionary with (path,filename) tuples
#as keys and a reason string as values

#abstract
#list songs, pick music folder if None
#read brokenfile,settingsfile,metadatafile
#PLAY MUSIC
#write settings, broken, metadata

#tidbits and todo
#hotkey definitions should be up here
#volume up can be optimized
#remove non-essential print statements
#store brokenlist sorted?
#put constants in another file and import them

######################################################################
######################################################################

c = { #constants
	"storagedir" : "storage"
	"settingsfile" : "settings.json",
	"metadatafile" : "metadata.json",
	"recordingfile" : "recording.wav",
	"reason" : "Where is your music located?"
}
#try to read settings from file first
settings = {
	"volume" : 0.5,
	"musicdir" : fileman.pickFolder(c['reason']),
}

iv = { #instance variables
	songnum = 0,
	playing = True,
	alive = True,
	killcount = 0,
}
metadata = {}
broken = set()


fileman.cd(settings['musicdir'])
songs = fileman.listFiles('')
random.shuffle(songs)
fileman.cd(os.getcwd()+os.sep+c['storagedir'])
broken = set(fileman.read('',c['brokenfile'],'').split('\n'))
#this no longer works
songs = list(set(songs)-broken)



#these need to be transplanted
fileman.write('',c['settingsfile'],json.dumps(settings))
fileman.write('',c['metadatafile'],json.dumps(metadata))


#on exit
#possibly sort broken and save it sorted
print(killcount,'songs have been added to broken.txt')
fileman.write('',c['brokenfile'],json.dumps(broken))


##################################################################
##################################################################


def playPause():
    global playing
    if playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    playing = not playing

def volDown():
    global volume
    volume = volume * 0.9
    if volume <= 0.0:
        volume = 0.001
    pygame.mixer.music.set_volume(volume)

def volUp():
    global volume
    volume = volume * 1.1
    if volume >= 1.0:
        volume = 1.0
    pygame.mixer.music.set_volume(volume)

def loadNplay():
	global songnum,songs,musicdir,sep,volume
	songnum = songnum % len(songs)
	songpath = ""+musicdir+sep+songs[songnum]
	try:
		song = mutagen.mp3.MP3(songpath)
		if pygame.mixer.get_init()[0] != song.info.sample_rate:
			pygame.mixer.quit()
			pygame.mixer.init(frequency=song.info.sample_rate)
		pygame.mixer.music.load(songpath)
		pygame.mixer.music.set_volume(volume)
		print('song',songnum,'---',songs[songnum])
		pygame.mixer.music.play(0)
	except Exception as e:
		print(e)
		markBroken()

def prev():
	global songnum
	songnum-=1
	song = songs[songnum]
	if song not in broken:
		if song not in metadata:
			metadata[song]={}
		if 'skips' in metadata[song]:
			metadata[song]['skips']-=1
			if metadata[song]['skips']<0:
				metadata[song]['skips']=0
	songnum-=1 #this is to counteract the +1 that will happen when the inner main loop quits
	pygame.mixer.music.stop()

def markBroken():
	global broken, songs, metadata, songnum, killcount
	song = songs[songnum]
	broken.add(song)
	songs.remove(song)
	metadata.pop(song,None)
	killcount+=1
	print(song,'has been marked as broken and benched')
	songnum-=1
	pygame.mixer.music.stop()

def next():
	global songs,songnum,metadata
	song = songs[songnum]
	if song not in broken:
		if song not in metadata:
			metadata[song]={}
		if 'skips' in metadata[song]:
			metadata[song]['skips']+=1
		else:
			metadata[song]['skips']=1
	pygame.mixer.music.stop()

searchHotkey = 'ctrl+shift+f'
def searchThenPlay():
	global songnum
	lap()
	rec(searchHotkey,recordingfile)
	print('listening took ',lap(),' seconds')
	transcription = transcribe(recordingfile)
	print('transcribing took ',lap(),' seconds and I think you said ',transcription)
	found = search(transcription,[s[:-4] for s in songs])
	print('searching took ',lap(),' seconds and found the song ',found)
	index = songs.index(found+'.mp3')
	if isinstance(index,int):
		songnum=index-1
		next()



def quit():
	global alive
	print('exiting...')
	alive = False

keyboard.add_hotkey('ctrl+shift+q',quit,args=())
keyboard.add_hotkey('ctrl+down',playPause,args=())
keyboard.add_hotkey('ctrl+shift+plus',volUp,args=())
keyboard.add_hotkey('ctrl+shift+-',volDown,args=())
keyboard.add_hotkey('ctrl+right',next,args=())
keyboard.add_hotkey('ctrl+left',prev,args=())
keyboard.add_hotkey('ctrl+shift+x',markBroken,args=())
keyboard.add_hotkey(searchHotkey,searchThenPlay,args=())


pygame.mixer.init()
while alive == True:
	loadNplay()
	while pygame.mixer.music.get_busy() and alive == True:
		pass
	songnum = songnum + 1
pygame.mixer.music.stop()
saveMetadata()
saveSettings()
saveBrokenList()
pygame.mixer.quit()
print('goodbye.')
    
    
    