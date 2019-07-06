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

#gameplan for tomorrow.
#add a method to fileman that gets a list of filename,relative_path tuples from a relativeRoot
#do repeated substitution on this top half until it is shrunk
#possibly add support for multiple music directories
#volume up and down can be made 2 lines shorter each with min() and max()
#all the hotkey definitions should be in settings
#remove nonessential print statements
c = { #constants
	"storagedir" : "storage"
	"settingsfile" : "settings.json",
	"metadatafile" : "metadata.json",
	"recordingfile" : "recording.wav",
	"reason" : "Where is your music located?"
}
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
#i'm not sure where to put these.
#they are changable but also persistient
#furthermore, they are large enough to be their own files most times
metadata = {}
broken = set()



######################################################################
######################################################################
######################################################################
######################################################################

#go through and figure out what all operations are performed on songs
#set math (subtracting broken)
#get length
#access element by songnum
#remove element by songname



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


#this needs to be analyized real good, taken apart, and destroyed
def saveBrokenList():
	global broken
	broken = set(sorted(broken))
	print(killcount,'songs have been added to broken.txt')
	if os.path.isfile(brokenfile):
		os.remove(brokenfile)
	with open(brokenfile,'w',encoding='utf-8') as f:
		for b in broken:
			f.write(b+nl)


if os.path.isdir(storagedir):
	if os.path.isfile(settingsfile):
		with open(settingsfile,'r') as f:
			settings = json.loads(f.read())
			musicdir = settings['musicdir']
			musicdirname = settings['musicdirname']
			volume = settings['volume']
	else:
		initSettingsFile()
	if os.path.isfile(metadatafile):
		f = open(metadatafile,'r')
		metadata = json.loads(f.read())
		f.close()
	else:
		initMetadataFile()
	if os.path.isfile(brokenfile):
		with open(brokenfile,'r',encoding='utf-8') as f:
			broken = set([element.replace(nl,'') for element in f.readlines()])
	else:
		initBrokenList()
else:
	os.makedirs(storagedir)
	initSettingsFile()
	initMetadataFile()
	initBrokenList()





##################################################################
##################################################################
##################################################################
##################################################################
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
    
    
    