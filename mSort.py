import os
import json
import random
import pygame
import keyboard

sep = os.path.sep
localdir = os.path.expanduser('~'+sep+'desktop')
storagedir = localdir+sep+'mSortLocalData'
settingsfile = storagedir+sep+'settings.json'
metadatafile = storagedir+sep+'metadata.json'
musicdir = ''
musicdirname = ''

settings = {}
metadata = {}
volume = 0.5
songnum = 0
playing = False
alive = True


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
	print(metadata)
	json_data = json.dumps(metadata)
	f = open(metadatafile,"w+")
	f.write(json_data)
	f.close()

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
	songnum-=1
	song = songs[songnum]
	if song not in metadata:
		metadata[song]={}
	if 'skips' in metadata[song]:
		metadata[song]['skips']-=1
		if metadata[song]['skips']<0:
			metadata[song]['skips']=0
	songnum-=1 #this is to counteract the +1 that will happen when the inner main loop quits
	pygame.mixer.music.stop()

def next():
	global songs,songnum,metadata
	song = songs[songnum]
	if song not in metadata:
		metadata[song]={}
	if 'skips' in metadata[song]:
		metadata[song]['skips']+=1
	else:
		metadata[song]['skips']=1
	pygame.mixer.music.stop()

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

while alive == True:
	loadNplay()
	while pygame.mixer.music.get_busy() and alive == True:
		pass
	songnum = songnum + 1

pygame.mixer.music.stop()
saveMetadata()
saveSettings()
pygame.mixer.quit()
    
    
    