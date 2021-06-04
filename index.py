#import text-to-speech conversion library in Python
import pyttsx3
engine =pyttsx3.init()

#import date-time library
import datetime

#Set the voice type and speed
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voice_rate=160
engine.setProperty('rate',voice_rate)

#function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak(" Hello! This is AI Assistant Clara, Welcome!")

#time function in h-m-s format
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
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
