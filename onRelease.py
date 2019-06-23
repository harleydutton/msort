import keyboard as k


alive = True
def quit():
	global alive
	alive = False

def myfun():
	print('pressed')
	while(k.is_pressed('ctrl+shift+f')):
		pass
	print('released')


k.add_hotkey('ctrl+shift+f',myfun,args=())
k.add_hotkey('ctrl+shift+q',quit,args=())


while(alive):
	pass