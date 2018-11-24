import os
import json

sep = os.path.sep

rootpath = os.path.dirname(os.path.realpath(__file__))
datafolder = rootpath+sep+'data'
settingsfile = datafolder+sep+'settings.json'
musicfolder = ''
musicfoldername = ''
settings = {}
def initSettings():
    global musicfolder
    global musicfoldername
    global settings
    musicfoldername = input('What is the name of the folder with your music?\n')
    musicfolder = rootpath+sep+musicfoldername
    settings['musicfolder'] = musicfolder
    settings['musicfoldername'] = musicfoldername
    json_data = json.dumps(settings)
    f = open(settingsfile,"w+")
    f.write(json_data)
    f.close()
if os.path.isdir(datafolder):
    if os.path.isfile(settingsfile):
        f = open(settingsfile,'r')
        if f.mode == 'r':
            settings = json.loads(f.read())
            musicfolder = settings['musicfolder']
            musicfoldername = settings['musicfoldername']
    else:
        initSettings()
else:
    os.makedirs(datafolder)
    initSettings()
repairfolder = rootpath+sep+musicfoldername+'-repair'
upvotefolder = rootpath+sep+musicfoldername+'-upvote'
downvotefolder = rootpath+sep+musicfoldername+'-downvote'

print('root path is {}'.format(rootpath))
print('data folder is {}'.format(datafolder))
print('settings file is {}'.format(settingsfile))
print('music folder is {}'.format(musicfolder))
print('music folder name is {}'.format(musicfoldername))
print('upvote folder is {}'.format(upvotefolder))
print('downvote folder is {}'.format(downvotefolder))
print('repair folder is {}'.format(repairfolder))




