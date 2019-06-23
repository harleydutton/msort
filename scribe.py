import speech_recognition as sr
def transcribe(path):
	r = sr.Recognizer()
	with sr.AudioFile(path) as source:
		audio = r.record(source)
	try:
		string = r.recognize_google(audio)
		return string
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))