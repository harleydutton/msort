import os
import json
import pygame
import random

sep = os.path.sep

#this will probably need to change for android
#localdir = os.path.dirname(os.path.realpath(__file__))
localdir = os.path.expanduser('~'+sep+'desktop')

storagedir = localdir+sep+'data'
settingsfile = storagedir+sep+'settings.json'

musicdir = ''
musicdirname = ''
settings = {}

def initSettings():
    global musicdir
    global musicdirname
    global settings
    musicdirname = input('What is the name of the folder with your music? ')
    musicdir = localdir+sep+musicdirname
    settings['musicdir'] = musicdir
    settings['musicdirname'] = musicdirname
    json_data = json.dumps(settings)
    f = open(settingsfile,"w+")
    f.write(json_data)
    f.close()

if os.path.isdir(storagedir):
    if os.path.isfile(settingsfile):
        f = open(settingsfile,'r')
        if f.mode == 'r':
            settings = json.loads(f.read())
            #breaks if the key names are wrong. add an exception
            musicdir = settings['musicdir']
            musicdirname = settings['musicdirname']
            f.close()
    else:
        initSettings()
else:
    os.makedirs(storagedir)
    initSettings()

if not os.path.isdir(musicdir):
    print('musicdir does not exist.')
    os.remove(settingsfile)
    exit()

print('storage dir is {}'.format(storagedir))
print('music folder is {}'.format(musicdir))


#this does not find songs recursively.
songs = [f for f in os.listdir(musicdir) if os.path.isfile(os.path.join(musicdir,f))]
random.shuffle(songs)
print(len(songs),'songs found')

songnum = 0
playing = False
volume = 0.5

pygame.init()
pygame.display.set_mode((200,100))

while True:
    try:        
        pygame.mixer.music.load(""+musicdir+sep+songs[songnum])
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(0)
        print('song',songnum,'---',songs[songnum])
        playing = True

        while pygame.mixer.music.get_busy():
            #pygame.event.poll()
            pygame.event.pump()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            if pygame.key.get_pressed()[pygame.K_n]:
                break
            if pygame.key.get_pressed()[pygame.K_KP_PLUS]:
                volume = volume + 0.01
                if volume >= 1.0:
                    volume = 1.0
                pygame.mixer.music.set_volume(volume)
            if pygame.key.get_pressed()[pygame.K_KP_MINUS]:
                volume = volume - 0.01
                if volume <= 0.0:
                    volume = 0.0
                pygame.mixer.music.set_volume(volume)
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit(0)
    except Exception as e:
        print('error:',e,songs[songnum])
    songnum=songnum+1
    songnum=songnum%len(songs)



