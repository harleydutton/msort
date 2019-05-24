import os
import json
import random
import pygame
import keyboard

sep = os.path.sep

localdir = os.path.expanduser('~'+sep+'desktop')

storagedir = localdir+sep+'data'
settingsfile = storagedir+sep+'settings.json'
metadatafile = storagedir+sep+'metadata.json'

musicdir = ''
musicdirname = ''
settings = {}
metadata = {}

def initSettingsFile():
    global musicdir, musicdirname, settings
    musicdirname = input('What is the name of the folder with your music? ')
    musicdir = localdir+sep+musicdirname
    settings['musicdir'] = musicdir
    settings['musicdirname'] = musicdirname
    json_data = json.dumps(settings)
    f = open(settingsfile,"w+")
    f.write(json_data)
    f.close()

def initMetadataFile():
	global metadata
	json_data = json.dumps(metadata)
	f = open(metadatafile,'w+')
	f.write(json_data)
	f.close()

if os.path.isdir(storagedir):
    if os.path.isfile(settingsfile):
        f = open(settingsfile,'r')
        if f.mode == 'r':
            settings = json.loads(f.read())
            musicdir = settings['musicdir']
            musicdirname = settings['musicdirname']
            f.close()
    else:
        initSettingsFile()
    if os.path.isfile(metadatafile):
    	f = open(metadatafile,'r')
    	metadata = json.loads(f.read())
    	f.close()
    else:
    	initMetadataFile()
else:
    os.makedirs(storagedir)
    initSettingsFile()
    initMetadataFile()

if not os.path.isdir(musicdir):
    print('musicdir does not exist.')
    os.remove(settingsfile)
    exit()

print('storage dir is {}'.format(storagedir))
print('music folder is {}'.format(musicdir))

songs = [f for f in os.listdir(musicdir) if os.path.isfile(os.path.join(musicdir,f))]
random.shuffle(songs)
print(len(songs),'songs found')

songnum = 0
playing = False
volume = 0.5
alive = True


pygame.mixer.init()

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
	try:
		pygame.mixer.music.load(""+musicdir+sep+songs[songnum])
		pygame.mixer.music.set_volume(volume)
		print('song',songnum,'---',songs[songnum])
		pygame.mixer.music.play(0)
	except Exception as e:
		print(e,'--',songs[songnum])

def prev():
	global songnum
	songnum = songnum - 2
	pygame.mixer.music.stop()

def next():
	pygame.mixer.music.stop()

def quit():
	global alive
	print('exiting...')
	alive = False

keyboard.add_hotkey('ctrl+shift+x',quit,args=())
keyboard.add_hotkey('ctrl+down',playPause,args=())
keyboard.add_hotkey('ctrl+shift+plus',volUp,args=())
keyboard.add_hotkey('ctrl+shift+-',volDown,args=())
keyboard.add_hotkey('ctrl+right',next,args=())
keyboard.add_hotkey('ctrl+left',prev,args=())

while alive == True:
	loadNplay()
	while pygame.mixer.music.get_busy() and alive == True:
		pass
	songnum = songnum + 1

pygame.mixer.music.stop()
pygame.mixer.quit()
    
    
    