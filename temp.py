import keyboard as k
import os
from fuzzywuzzy import fuzz
from record import rec
from scribe import transcribe
from datetime import datetime as dt
import search

musicdir = 'C:\\Users\\Harley\\desktop\\music - Copy'
songs = [f for f in os.listdir(musicdir) if os.path.isfile(os.path.join(musicdir,f))]
print('num',len(songs))
hotkey = 'ctrl+shift+f'
filepath = 'c:\\users\\harley\\desktop\\msortlocaldata\\temp.wav'




#OPTIMIZATION IDEAS
#look into multithreading

#the list can be slipt over processors
#searching for artist/title/album can all be separate jobs

#if you find the theoretical max for a category you can be done with your list



def fun1():
	def fun2(hk,fp):
		start = dt.now()
		os.remove(filepath)
		rec(hk,fp)
		print(search.searchA(transcribe(fp),[s[:-4] for s in songs]))
		end = dt.now()
		elapsed=end-start
		print(elapsed.total_seconds())
	return fun2


k.add_hotkey(hotkey,fun1(),args=(hotkey,filepath))


alive = True
def quit():
	global alive
	alive = False
k.add_hotkey('ctrl+shift+q',quit,args=())
while(alive):
	pass