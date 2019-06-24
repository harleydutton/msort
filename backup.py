import keyboard
import speech_recognition as sr
import os
import sounddevice as sd
import wavio
from datetime import datetime



print('found {} songs'.format(len(songs)))

alive = True
def quit():
	global alive
	alive = False

def search(s):
	setout = ''
	setlargest = 0
	for song in songs:
		setl = fuzz.token_set_ratio(song[0:-4].lower(),s.lower())
		print('{} is a {}%  set match with {}'.format(s,setl,song))
		if setl > setlargest:
			setout = song
			setlargest = setl
			print('best set match is {} with {}%'.format(setout,setlargest))
	print(setlargest)
	return [setout,setlargest]


def doTheThing():
	start = datetime.now()
	print('doing the thing!')
	fs=44100
	duration = 5
	myrecording = sd.rec(fs * duration, samplerate=fs, channels=2)
	print("Recording Audio")
	sd.wait()
	wavio.write('temp.wav',myrecording,fs,sampwidth=2)
	temp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp.wav")
	print(temp)
	r = sr.Recognizer()
	with sr.AudioFile(temp) as source:
	    audio = r.record(source)
	try:
	    query = r.recognize_google(audio)
	    print(search(query))
	    print("Google Speech Recognition thinks you said " + query)
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	end = datetime.now()
	elapsed = end - start
	print('took about {} units of time'.format(elapsed.total_seconds()))



keyboard.add_hotkey('ctrl+shift+space',print,args=('poop'))
keyboard.add_hotkey('ctrl+shift+f',doTheThing,args=())
keyboard.add_hotkey('ctrl+shift+q',quit,args=())

while(alive):
	pass