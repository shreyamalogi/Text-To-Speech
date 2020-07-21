#TEXT TO SPEECH
from gtts import gTTS

text = input ("Enter the text:")
lang = 'en'

tts = gTTS(text=text ,lang=lang)
tts.save("SpeechOutput.mp3")
#mpyg321 library to play this from python