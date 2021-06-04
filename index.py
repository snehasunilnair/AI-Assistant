#import text-to-speech conversion library in Python
import pyttsx3
engine =pyttsx3.init()

#import speech recognition to take commands from user
import speech_recognition as sr

#import wikipedia
import wikipedia

#import date-time library
import datetime

#Set the voice type,speed and volume
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voice_rate=170
engine.setProperty('rate',voice_rate)
volume = engine.getProperty('volume')
vol = 0.7
engine.setProperty('volume', vol)

#function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#time function in h-m-s format
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    speak("The current time is")
    speak(Time)

#date function in dd-mm-yyyy format
def date():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

#greeting function
def greet():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("This is AI Assistant Lily, How can I help you?")

#Take command from user using speech recognition feature
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio)
        
    except Exception as e:
        print(e)
        speak("Say that again please..")
        return"None"
    return query

#main function
if __name__  in "__main__":
    greet()
    while True:
        query = takeCommand().lower()
        print("Query : ",query)
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("Searching...")
            query= query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            speak(result)

        elif "offline" in query or "thank you" in query or "exit" in query:
            quit()
    