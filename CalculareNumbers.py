import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wolframAlpha (query):
    apikey ="T6Q8LK-RV7QYLA2HH"
    request =wolframalpha.Client(apikey)
    requested = request.query(query)    

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def calc(query):
    term = str(query)
    term = term.replace("jarvis","")
    term = term.replace("multiply","*")
    term = term.replace("into","*")
    term = term.replace("plus","+")
    term = term.replace("minus","-")
    term = term.replace("divide","/")

    final = str(term)
    try:
        result = wolframAlpha(final)
        print(result)
        speak(result)
    except:
        speak("The value is not answerable")    