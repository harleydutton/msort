import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy
import keyboard as k
import os
mic = sd.query_devices(None, 'input')
samplerate = int(mic['default_samplerate'])
channels = mic['max_input_channels']
q = queue.Queue()
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())
def rec(hotkey,filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    with sf.SoundFile(filepath, mode='x', samplerate=samplerate, channels=channels, subtype=None) as file:
        with sd.InputStream(samplerate=samplerate, device=None, channels=channels, callback=callback):
            while (k.is_pressed(hotkey)):
                file.write(q.get())