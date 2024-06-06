from fnmatch import translate
from googletrans import Translator
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition
import os
from playsound import playsound
import time 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def translategl(query):
    speak("Sure sir")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate ")
    lang = input("To lang : ")
    text_to_translate = translator.translate(query, src="auto",dest=lang)
    text = text_to_translate.text
    try:
        speakgl = gTTS(text=text,lang=lang, slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(3)
        os.remove("voice.mp3")
    except :
        print("Unable to translate")    