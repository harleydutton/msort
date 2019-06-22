import keyboard
import os
import random
from fuzzywuzzy import fuzz

musicdir = 'C:\\Users\\Harley\\desktop\\music - Copy'
songs = [f for f in os.listdir(musicdir) if os.path.isfile(os.path.join(musicdir,f))]
print('num',len(songs))
print(songs)

# songs = ['Bad Apple!! - JubyPhonic.mp3', 'Feel It Still - Portugal. The Man.mp3', 'Forest Whitiker - Brother Ali.mp3', 'Fox on the Run - The Sweet.mp3', 'From the Inside - Linkin Park.mp3', 'Für Elise - Beethoven.mp3', 'Gangnam Style - PSY.mp3', 'Get Jinxed - Djerv.mp3', 'Give Me Something - Seafret.mp3', 'Gives You Hell - The All‐American Rejects.mp3', 'Gold - Kiiara.mp3', 'Gravity Falls - Brad Breeck.mp3', 'Hot Mess - Cobra Starship.mp3', 'House of Gold - Twenty One Pilots.mp3', 'How Do You Do_ - Boom!.mp3', 'How Far I_ll Go - Any Gabrielly.mp3', 'How to Save a Life - The Fray.mp3', 'Moonage Daydream - David Bowie.mp3', 'People Get Ready - The Impressions.mp3', 'Piano Man - Billy Joel.mp3', 'Pinball Wizard - The Who.mp3']


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
def search(s):
	out = ''
	largest=0 
	for song in songs:
		l = max(fuzz.token_set_ratio(song[0:-4].lower(),s.lower()),fuzz.partial_ratio(song[0:-4].lower(),s.lower()))
		print('dist between {} and {} is {}'.format(s,song,l))
		print('l',l,'largest',largest)
		if l > largest:
			out = song
			largest = l
			print('new largest is {} with a distance of {}'.format(out,largest))
	return out






# def queryConcat(c):
# 	global query
# 	query+=c
# 	print(query)
# def removeLast():
# 	global query
# 	query = query[0:-1]
# 	print(query)
# def addCharListener(c):
# 	hotkeylist.append(keyboard.add_hotkey(c,queryConcat,args=(c),suppress=True))
# def addShiftedListener(c):
# 	hotkeylist.append(keyboard.add_hotkey(c+"+shift",queryConcat,args=(c),suppress=True))
# def hookEmUp(key,function):
# 	return hotkeylist.append(keyboard.on_press_key(key,function))
# def function2():
# 	for f in foo+bar+'= +':
# 		hookEmUp(f,hardcodeQueryAddon(f))
# def hardcodeQueryAddon(key):
# 	def add2Query():
# 		global query
# 		query+=key
# 		print(query)
# 	return add2Query
# def unhook():
# 	global hotkeylist, query
# 	for h in hotkeylist:
# 		keyboard.remove_hotkey(h)
# 	hotkeylist = []
# 	keyboard.remove_hotkey('enter')
# 	print('query: ',query)
# 	print(search(query))
# 	query = ''
# def listen():
# 	global hotkeylist
# 	print('type a wuery and hit enter')
# 	function2()
# 	for c in foo:
# 		addCharListener(c)
# 		addShiftedListener(shifted[c])
# 	keyboard.add_hotkey('enter',unhook,args=())








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