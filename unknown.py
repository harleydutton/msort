import argparse
import tempfile
import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy
assert numpy
import keyboard as k
import os
from scribe import transcribe
#def exportedcallback(path,input):

path = 'c:\\users\\harley\\desktop\\msort\\'
hotkey = 'ctrl+shift+f'


filename=path+'temp.wav'
mic = sd.query_devices(None, 'input')
samplerate = int(mic['default_samplerate'])
channels = mic['max_input_channels']

q = queue.Queue()
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def startstop():
    with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=channels, subtype=None) as file:
        with sd.InputStream(samplerate=samplerate, device=None, channels=channels, callback=callback):
            while (k.is_pressed(hotkey)):
                file.write(q.get())
    print(filename)
    print('transcription:{}'.format(transcribe(filename)))
    os.remove(filename)

alive = True
def quit():
    global alive
    alive = False

k.add_hotkey('ctrl+shift+q',quit,args=())
k.add_hotkey(hotkey,startstop,args=())

while(alive):
    pass