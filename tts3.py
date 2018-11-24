from gtts import gTTS
tts = gTTS('hello')
tts.save('hello.mp3')






#use
#gtts-cli 'hello' --output hello.mp3
#to create .mp3's from the command line.

#once you have made them you have to figure out how to play them yourself

tts2 = gTTS('open mike eagle. ziggy starfish. anti-anxiety raps. prod. gold panda.')
tts2.save('songnametest.mp3')
