import os
import json
sep = os.path.sep

rootpath = os.path.dirname(os.path.realpath(__file__))
datafolder = rootpath+sep+'data'
settingsfile = datafolder+sep+'settings.json'
print('root path is {}'.format(rootpath))
print('data folder is {}'.format(datafolder))
print('settings file is {}'.format(settingsfile))
def initSettings():
    musicfolder = rootpath+sep+input('What is the name of the folder with your music?\n')
    settings = {}
    settings['musicfolder'] = musicfolder
    json_data = json.dumps(settings)
    #save the json data to settingsfile
    print(json_data)
if os.path.isdir(datafolder):
    if os.path.isfile(settingsfile):
        #load up the file options/settins/temp file and set the music folder.
        a = 0
    else:
        initSettings()
else:
    os.makedirs(datafolder)
    initSettings()
print(musicfolder)
#currently running into a scope issue: musicfolder ceases to be





