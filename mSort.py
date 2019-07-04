import os
import json
import random
import pygame
import keyboard
import mutagen.mp3
from search import search
from scribe import transcribe
from record import rec
from datetime import datetime as dt
from stopwatch import lap

sep = os.path.sep
nl = '\n'
localdir = os.path.expanduser('~'+sep+'desktop')
storagedir = localdir+sep+'mSortLocalData'
brokenfile = storagedir+sep+'broken.txt'
settingsfile = storagedir+sep+'settings.json'
metadatafile = storagedir+sep+'metadata.json'
recordingfile = storagedir+sep+'recording.wav'
musicdir = ''
musicdirname = ''

settings = {}
metadata = {}
broken = set()
volume = 0.5
songnum = 0
playing = True
alive = True
killcount = 0

def saveSettings():
	settings['volume'] = volume
	settings['musicdir'] = musicdir
	settings['musicdirname'] = musicdirname
	json_data = json.dumps(settings)
	f = open(settingsfile,"w+")
	f.write(json_data)
	f.close()

def saveMetadata():
	print('saving metadata...')
	json_data = json.dumps(metadata)
	f = open(metadatafile,"w+")
	f.write(json_data)
	f.close()

def saveBrokenList():
	global broken
	broken = set(sorted(broken))
	print(killcount,'songs have been added to broken.txt')
	if os.path.isfile(brokenfile):
		os.remove(brokenfile)
	with open(brokenfile,'w',encoding='utf-8') as f:
		for b in broken:
			f.write(b+nl)

def initBrokenList():
	saveBrokenList()

def initSettingsFile():
	global musicdir, musicdirname, settings
	musicdirname = input('What is the name of the folder with your music? ')
	musicdir = localdir+sep+musicdirname
	saveSettings()

def initMetadataFile():
	global metadata
	json_data = json.dumps(metadata)
	f = open(metadatafile,'w+')
	f.write(json_data)
	f.close()

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

if not os.path.isdir(musicdir):
    print('musicdir does not exist.')
    os.remove(settingsfile)
    exit()

print('storage dir is {}'.format(storagedir))
print('music folder is {}'.format(musicdir))
print('broken file is {}'.format(brokenfile))
print('volume is {}'.format(volume))

songs = [f for f in os.listdir(musicdir) if os.path.isfile(os.path.join(musicdir,f))]
random.shuffle(songs)
print(len(songs),'songs found')

print(len(broken),'songs to be removed due to damage')
print(broken)
songs = list(set(songs)-broken)
print(len(songs),'songs remain')

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
    
    
    