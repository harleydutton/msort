import pygame
from os import listdir
from os.path import isfile,join,exists,isdir

path = 'C:\\Users\\harley\\Desktop\\music\\aug30.2018\\'
print('path'+path)

songs = [f for f in listdir(path) if isfile(join(path, f))]
folders = [f for f in listdir(path) if isdir(join(path, f))]

print('folders:')
print(folders)
print('songs:')
print(songs[0])
print(path+songs[0])

try:
    pygame.init()
    pygame.display.set_mode((200,100))
    pygame.mixer.music.load(""+path+songs[0])
    pygame.mixer.music.play(0)
    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
except Exception as e:
    print("error:",e)


#loop while you have songs to play
        #play a song
        #once it is done wait for input and play a tone


#take input the whole time
