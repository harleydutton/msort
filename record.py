import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy
import keyboard as k
import os
from scribe import transcribe
mic = sd.query_devices(None, 'input')
samplerate = int(mic['default_samplerate'])
channels = mic['max_input_channels']
q = queue.Queue()
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())
def rec(hotkey,filepath):
    with sf.SoundFile(filepath, mode='x', samplerate=samplerate, channels=channels, subtype=None) as file:
        with sd.InputStream(samplerate=samplerate, device=None, channels=channels, callback=callback):
            while (k.is_pressed(hotkey)):
                file.write(q.get())
    # I think we might want to stop here and let some other program handle the transcription and removel
    # print('transcription:{}'.format(transcribe(filepath)))
    # os.remove(filepath)