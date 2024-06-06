import pyttsx3
import speech_recognition
import random

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
        print("Recognizing..")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def play_game():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i =0
    my_score = 0
    com_score = 0
    tie =0

    while(i<5):
        choose = ("rock","paper","scissor")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if query =="none":
            speak("Say that again")
            i -=1
        elif (query == "rock" or query == "lock"):
            if (com_choose =="rock"):
                speak("Rock")
                speak("Match tie")
                tie +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")
            elif (com_choose == "paper"):
                speak("Paper")
                speak("Computer won")
                com_score +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")
            else:
                speak("Scissor")    
                speak("You won")
                my_score +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")
        elif (query == "paper" ):
            if (com_choose =="rock"):
                speak("Rock")
                speak("You won")
                my_score +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")
            elif (com_choose =="paper"):
                speak("Paper")
                speak("Match tie")
                tie +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")
            else:
                speak("Scissor")    
                speak("Computer won")
                com_score +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")
        elif (query == "Scissor" or "Caesar"):
            if (com_choose =="rock"):
                speak("Rock")
                speak("Computer won")
                com_score +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")
            elif (com_choose =="paper"):
                speak("Paper")
                speak("You won")
                my_score +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")
            else:
                speak("Scissor")    
                speak("Match tie")
                tie +=1
                print(f"Score- My score : {my_score}, Computer score : {com_score}, No result : {tie}")

        i += 1
    print(f"FINAL SCORE :- You :- {my_score} : Computer :- {com_score}")