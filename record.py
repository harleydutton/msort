import keyboard as k
import sounddevice as sd
import wavio as w
import speech_recognition as sr
import os

alive = True
def quit():
	alive = False
k.add_hotkey('ctrl+shift+q',quit,args=())


#values, paramaters, inputs, and arguments
frequency = 44100
filename = 'temp.wav'
channels = 2
path = 'C:\\Users\\Harley\\Desktop\\music - Copy\\'





handle = sd.Stream()

def begin():
	handle.start()

def end():
	handle.stop()
	w.write(filename,handle,frequency,sampwidth=channels)
	loc = path+filename
	print('file loc is {}'.format(loc))

	r = sr.Recognizer()
	with sr.AudioFile(loc) as source:
		audio = r.record(source)
	try:
		query = r.recognize_google(audio)
		print('google transcription:{}'.format(query))
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))




k.add_hotkey('ctrl+shift+f',begin,args=())
k.add_hotkey('ctrl+shift+enter',end,args=())















while(alive):
	pass