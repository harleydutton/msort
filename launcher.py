import pygame
from os import listdir
from os.path import isfile,join,exists,isdir


#get the location of some local storage
storagedir = 'C:\\Users\\harley\\Desktop\\'
print("using "+storagedir+" as local storage for options and such")

#check if you have a path to a music folder
#if not open a filebrowser and let the user select one then save it
#then use the one that is saved
musicdir = 'C:\\Users\\harley\\Desktop\\music - Copy\\'
print("looking for music in "+musicdir)

#I dont think this is delving recursively. for now that is fine
songs = [f for f in listdir(musicdir) if isfile(join(musicdir, f))]
print('songs:')
print(songs[0])
print(musicdir+songs[0])

#what is this doing?
folders = [f for f in listdir(musicdir) if isdir(join(musicdir, f))]
print('folders:')
print(folders)


playing = False
try:
    pygame.init()
    pygame.display.set_mode((200,100))
    pygame.mixer.music.load(""+musicdir+songs[0])
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

