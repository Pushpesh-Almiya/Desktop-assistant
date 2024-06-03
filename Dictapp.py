import os
import pyautogui #press any key in keyboard
import webbrowser
import pyttsx3
from time import sleep 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"command prompt":"cmd", "paint":"paint", "word":"winword", "excel":"excel","chrome":"chrome","vs code":"code","powerpoint":"powerpnt"}

def openAppWeb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query :
        query = query.replace ("open","")
        query = query.replace ("jarvis","")
        query = query.replace ("launch","")
        query = query.replace (" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeAppWeb(query):
    speak("Closing, sir")
    if  "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")    
    elif "2 tabs" in query or "two tabs" in query:
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        speak("All tabs closed")
    elif "3 tabs" in query or "three tabs" in query:
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        speak("All tabs closed")
    elif "4 tabs" in query or "four tabs" in query:
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        speak("All tabs closed")
    elif "5 tabs" in query or "five tabs" in query:
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")   
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query :
                os.system(f"taskkill /f /im {dictapp[app]}.exe")