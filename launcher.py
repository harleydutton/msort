import pygame
from os import listdir
from os.path import isfile,join,exists,isdir

path = 'C:\\Users\\harley\\Desktop\\music workshop\\music - Copy\\'
#get the rootpath.
rootpath = 'C:\\Users\\harley\\Desktop\\music workshop\\'
#then prompt for the name of the music folder
musicfolder = ''
fixfolder = musicfolder+'-fix'
upvotefolder = musicfolder+'-upvote'
downvotefolder = musicfolder+'-downvote'
datafolder = 'data'
#make the log file, the options file, and store the sound files

print('path'+path)

songs = [f for f in listdir(path) if isfile(join(path, f))]
folders = [f for f in listdir(path) if isdir(join(path, f))]

print('folders:')
print(folders)
print('songs:')
print(songs[0])
print(path+songs[0])
playing = False

try:
    pygame.init()
    pygame.display.set_mode((200,100))
    pygame.mixer.music.load(""+path+songs[0])
    pygame.mixer.music.play(0)
    playing = True
    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if playing:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            playing = not playing
        if pygame.key.get_pressed()[pygame.K_q]:
            exit(0)


except Exception as e:
    print("error:",e)

