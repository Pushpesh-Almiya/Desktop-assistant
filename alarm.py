import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedTime = open ("Alarmtext.txt","rt")
time = extractedTime.read()
time = str(time)
extractedTime.close()

deleteTime = open("Alarmtext.txt","r+")
deleteTime.truncate(0)
deleteTime.close()

def ring (time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timeset.replace("set an alarm","")
    timenow = timeset.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        if currentTime == Alarmtime:
            speak("Alarm ringing, Sir")
            os.startfile("music.mp3")

        elif currentTime + "00:00:30" == Alarmtime:
            exit()
ring(time)            