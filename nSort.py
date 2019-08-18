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
#volume up can be optimized
#remove non-essential print statements
#put print messages in constants
#put constants in another file and import them?
#what about duplicate filenames in brokenlist 
#have fileman.cd normalize the path it stores.
#have all fileman relative_path arguments have a default of ''
#add a getter to fileman for the current directory
#make the .json files we write pretty
#redo keybinds with settings[Xhotkey]
#import fileman as fm
#can filepicker be written without the middleman? no tkinter window?

#formats for songs and brokenlist
# [('path','filename'),('path','filename'),...]
# {('path','filename'):'reason',('path','filename'):'reason',...}
######################################################################
######################################################################

c = { #constants
	"storagedir" : "storage"
	"settingsfile" : "settings.json",
	"brokenfile" : "broken.json",
	"metadatafile" : "metadata.json",
	"recordingfile" : "recording.wav",
	"reason" : "Where is your music located?"
}
iv = { #instance variables
	songnum = 0,
	playing = True,
	alive = True,
	killcount = 0
}
settings = {
	"volume" : 0.1,
	"musicdir" : None,
	"quitHotkey" : "ctrl+shift+q",
	"playPauseHotkey" : "ctrl+down",
	"nextHotkey" : "ctrl+right",
	"prevHotkey" : "ctrl+left",
	"volUpHotkey" : "ctrl+shift+plus",
	"volDownHotkey" : "ctrl+shift+-",
	"markBrokenHotkey" : "ctrl+shift+x",
	"searchHotkey" : "ctrl+shift+f"
}
metadata = {} 
broken = {} 

fileman.cd(os.getcwd()+os.path.sep+c['storagedir'])
settings = json.loads(fileman.readFile('',c['settingsfile'],default_data=json.dumps(settings)))
metadata = json.loads(fileman.readFile('',c['metadatafile'],default_data=json.dumps(metadata)))
broken = json.loads(fileman.readFile('',c['brokenfile'],default_data=json.dumps(broken)))
while settings['musicdir'] is None:
	settings['musicdir']=fileman.pickFolder(c['reason'])
fileman.cd(settings['musicdir'])
songs = random.shuffle(fileman.listFiles(''))
songs = list(set(songs)-set(broken.keys()))

def playPause():
    global playing
    if playing: pygame.mixer.music.pause()
    else: pygame.mixer.music.unpause()
    playing = not playing

def volDown():
    global volume
    volume = max(volume * 0.9,0.001)
    pygame.mixer.music.set_volume(volume)

def volUp():
    global volume
    volume = min(volume * 1.1,1.0)
    pygame.mixer.music.set_volume(volume)

def quit():
	global alive


##############################################################

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
pygame.mixer.quit()

if killcount: print(killcount,'songs have been added to broken.txt')
fileman.write('',c['brokenfile'],json.dumps(broken))
fileman.write('',c['settingsfile'],json.dumps(settings))
fileman.write('',c['metadatafile'],json.dumps(metadata))