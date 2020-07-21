import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone() as source:
     print("speak out: ")
     try:
         audio = rec.listen(source)
         text = rec.recognize_google(audio)
         print("You said:{}".format(text))
     except:
        print("Sorry,I couldn't Get you! ")
