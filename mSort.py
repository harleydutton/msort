import os
import json
sep = os.path.sep

rootpath = os.path.dirname(os.path.realpath(__file__))
datafolder = rootpath+sep+'data'
settingsfile = datafolder+sep+'settings.json'
print('root path is {}'.format(rootpath))
print('data folder is {}'.format(datafolder))
print('settings file is {}'.format(settingsfile))
musicfolder = ''
settings = {}
def initSettings():
    global musicfolder
    musicfolder = rootpath+sep+input('What is the name of the folder with your music?\n')
    global settings
    settings['musicfolder'] = musicfolder
    json_data = json.dumps(settings)
    f = open(settingsfile,"w+")
    f.write(json_data)
    f.close()
if os.path.isdir(datafolder):
    if os.path.isfile(settingsfile):
        #load up the file options/settins/temp file and set the music folder.
        f = open(settingsfile,'r')
        if f.mode == 'r':
            settings = json.loads(f.read())
            musicfolder = settings['musicfolder']
    else:
        initSettings()
else:
    os.makedirs(datafolder)
    initSettings()
print(musicfolder)





