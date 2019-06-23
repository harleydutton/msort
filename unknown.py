import argparse
import tempfile
import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy
import keyboard as k
from scribe import transcribe


def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument( '-l', '--list-devices', action='store_true', help='show list of audio devices and exit')
parser.add_argument( '-d', '--device', type=int_or_str, help='input device (numeric ID or substring)')
parser.add_argument( '-r', '--samplerate', type=int, help='sampling rate') 
parser.add_argument( '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument( 'filename', nargs='?', metavar='FILENAME', help='audio file to store recording to')
parser.add_argument( '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args()

if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
if args.samplerate is None:
    device_info = sd.query_devices(args.device, 'input')
    args.samplerate = int(device_info['default_samplerate'])
if args.filename is None:
    args.filename = tempfile.mktemp(prefix='delme_rec_unlimited_', suffix='.wav', dir='')

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def startstop():
    print('i have begun recording')
    with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate, channels=args.channels, subtype=args.subtype) as file:
        with sd.InputStream(samplerate=args.samplerate, device=args.device, channels=args.channels, callback=callback):
            while (k.is_pressed('ctrl+shift+f')):
                print('i am doing this thing')
                file.write(q.get())
    print('i have finished rcording')
    print(args.filename)
    print('this is what i think you said:{}'.format(transcribe(args.filename)))
    parser.exit(0)

alive = True
def quit():
    global alive
    alive = False

k.add_hotkey('ctrl+shift+q',quit,args=())
k.add_hotkey('ctrl+shift+f',startstop,args=())

while(alive):
    pass




