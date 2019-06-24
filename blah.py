from record import rec
import keyboard as k

fp = 'c:\\users\\harley\\desktop\\msort\\temp.wav'
h = 'ctrl+shift+f'

alive = True
def quit():
    global alive
    alive = False

k.add_hotkey('ctrl+shift+q',quit,args=())
k.add_hotkey(h,rec,args=(h,fp))

while(alive):
    pass