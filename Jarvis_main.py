import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui

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

#set alarm using jarvis
  
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break 

                #conversations 
                elif "say" in query:
                    query = query.replace("Jarvis", "")   
                    query = query.replace("say", "")   
                    query = query.replace("to", "")   
                    speak(query)

                elif 'hello' in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query or "i m fine" in query:
                    speak("That's great sir")
                elif "how are you" in query:
                    speak("perfect sir ")
                elif "thank you" in query or "thank" in query:
                    speak("You are welcome,sir. Feel free to ask anytime.")
                
                #Open/Close Apps with just your voice...
                #Easy method.........
                # elif "open" in query:
                #     query = query.replace("open","")
                #     query = query.replace("jarvis","")
                #     pyautogui.press("super")
                #     pyautogui.typewrite(query)
                #     pyautogui.sleep(2)
                #     pyautogui.press("enter")

                # elif "close" in query:
                #     speak("Closing, sir") 
                #     pyautogui.hotkey("ctrl","w") 

                elif "open" in query :
                    from Dictapp import openAppWeb
                    openAppWeb(query)

                elif "close" in query:
                    from Dictapp import closeAppWeb
                    closeAppWeb(query)    

                #Searching from web (Google, youtube, wiki)
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                #Temprature and weather 
                
                elif "temperature" in query:
                    search = "temperature in almora"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_= "BNeawe").text
                    speak(f"Current {search} is {temp}")

                elif "weather" in query:
                    search = "weather in almora"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    weather = data.find("div", class_= "BNeawe").text
                    speak(f"Current {search} is {weather}")

                elif "the time" in query :
                    strTime = datetime.datetime.now().strftime("%H:%M") 
                    speak (f"Sir, The current time is {strTime}")

                elif "the day" in query :
                    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                    strDay = datetime.datetime.now().weekday()
                    print (f"Today is: {days[strDay]}")
                    speak (f"Today is: {days[strDay]}")

                elif "the date" in query :
                    now = datetime.datetime.now()
                    formatted_date = now.strftime("%d-%B-%Y")
                    print("Today's date is:", formatted_date)
                    speak (f"Today's date is: {formatted_date}")

                elif "set an alarm" in query :
                    print("Input time example : 10 and 10 and 10")
                    speak("Set the time")
                    a= input("Please tell the time :- ")
                    # print (a)
                    alarm(a)
                    speak("Done, sir")

                #Fully automate YouTube controls.........
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video Paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video Played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Video unmuted")
                elif "volume up" in query:
                    from Keyboard import volumeUp
                    speak("Turning volume up,Sir")
                    volumeUp()
                elif "volume down" in query:
                    from Keyboard import volumeDown
                    speak("Turning volume down,Sir")
                    volumeDown()

                #Remember function....
                elif "remember that" in query:
                    rememberMsg = query.replace("remember that","")
                    rememberMsg = query.replace("jarvis","")
                    speak("You told me"+ rememberMsg)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMsg)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me" + remember.read())

                #Calculate function
                elif "calculate" in query:  
                    from CalculareNumbers import calc
                    query = query.replace("calculate","")    
                    query = query.replace("jarvis","")    
                    calc(query)

                #Shut down function
                elif "shut down" in query or "shutdown" in query:
                    speak("Are you sure you want to shutdown")
                    shutdown = input("Do you want to shut down your computer ? (yes/no):-")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                #Whatsapp message .....
                elif "whatsapp" in query :
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "finally sleep" in query: 
                    speak("Okay sir. Going to sleep.")
                    exit()   
