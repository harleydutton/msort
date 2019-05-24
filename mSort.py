import os
import json
import random
import keyboard
import simpleaudio

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

songwav = simpleaudio.WaveObject.from_wave_file(os.path.join(musicdir,songs[songnum]))
songwav.play()






# song = pydub.AudioSegment.from_wav(os.path.join(musicdir,songs[songnum]))
# play(song)


# playing = False
# volume = 0.5
# changeSong = False

# pygame.init()
# pygame.display.set_mode((200,100))

# keyboard.add_hotkey('ctrl+shift+q',exit,args=(0))

# def playPause():
#     global playing
#     if playing:
#         pygame.mixer.music.pause()
#     else:
#         pygame.mixer.music.unpause()
#     playing = not playing
# keyboard.add_hotkey('ctrl+down',playPause,args=())

# def volDown():
#     global volume
#     volume = volume * 0.9
#     if volume <= 0.0:
#         volume = 0.001
#     pygame.mixer.music.set_volume(volume)
# keyboard.add_hotkey('ctrl+shift+-',volDown,args=())

# def volUp():
#     global volume
#     volume = volume * 1.1
#     if volume >= 1.0:
#         volume = 1.0
#     pygame.mixer.music.set_volume(volume)
# keyboard.add_hotkey('ctrl+shift+plus',volUp,args=())

# def next():
#     global songnum, volume, musicdir, sep, songs, changeSong
#     songnum = songnum + 1
#     songnum = songnum % len(songs)
#     changeSong = False
#     try:
#         pygame.mixer.music.load(""+musicdir+sep+songs[songnum])
#         pygame.mixer.music.set_volume(volume)
#         print('song',songnum,'---',songs[songnum])
#         pygame.mixer.music.play(0)
#         playing = True
#         while pygame.mixer.music.get_busy():
#             pass
#     except Exception as e:
#         print(e,'--',songs[songnum])
#     if changeSong == False:
#         next()
# def skip():
#     global changeSong
#     changeSong = True
#     next()
# keyboard.add_hotkey('ctrl+right',skip,args=())

# next()
#def prev():

# while True:
#     try:      
#         next()
#         while pygame.mixer.music.get_busy():
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     exit(0)
    
    