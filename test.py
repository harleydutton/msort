import keyboard
import os
import stringdist
import random

musicdir = 'C:\\Users\\Harley\\desktop\\brokenMixedIn'
songs = [f for f in os.listdir(musicdir) if os.path.isfile(os.path.join(musicdir,f))]
print('num',len(songs))

# def record():
# 	print('type your query and hit enter')
# 	for word in keyboard.get_typed_strings(keyboard.record('enter',True,False),True):
# 		print(word)
# keyboard.add_hotkey('ctrl+shift+f',record,args=())


foo = "`1234567890-qwertyuiop][asdfghjkl;zxcvbnm,./\\'"
bar = "~!@#$%^&*()_QWERTYUIOP}{ASDFGHJKL:ZXCVBNM<>?|\""
shifted = {}
for f, b in zip(foo,bar):
	shifted[f]=b



query = ''
hotkeylist = []
def queryConcat(c):
	global query
	query+=c
	print(query)

def removeLast():
	global query
	query = query[0:-1]
	print(query)

def addCharListener(c):
	hotkeylist.append(keyboard.add_hotkey(c,queryConcat,args=(c),suppress=True,timeout=11))

def addShiftedListener(c):
	hotkeylist.append(keyboard.add_hotkey(c+"+shift",queryConcat,args=(c),suppress=True,timeout=11))

def unhook():
	global hotkeylist, query
	for h in hotkeylist:
		keyboard.remove_hotkey(h)
	hotkeylist = []
	keyboard.remove_hotkey('enter')
	print('query: ',query)
	query = ''

def listen():
	global hotkeylist
	hotkeylist.append(keyboard.add_hotkey('=+shift',queryConcat,args=('+'),suppress=True,timeout=.10))
	hotkeylist.append(keyboard.add_hotkey('=',queryConcat,args=('='),suppress=True,timeout=.10))
	hotkeylist.append(keyboard.add_hotkey('space',queryConcat,args=(' '),suppress=True,timeout=.10))
	hotkeylist.append(keyboard.add_hotkey('backspace',removeLast,args=(),suppress=True,timeout=.1))
	for c in foo:
		addCharListener(c)
		addShiftedListener(shifted[c])
	keyboard.add_hotkey('enter',unhook,args=())



kill = True
def quit():
	global kill
	kill = False

def dosomething():
	print(random.random())


keyboard.add_hotkey('ctrl+shift+f',listen,args=())
keyboard.add_hotkey('ctrl+shift+q',quit,args=())
keyboard.add_hotkey('ctrl+space',dosomething,args=())

while(kill):
	pass