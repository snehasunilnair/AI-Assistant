#Importing the text-to-speech conversion library in Python
import pyttsx3
engine =pyttsx3.init()

#Set the voice type and speed
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voice_rate=160
engine.setProperty('rate',voice_rate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak(" Hello! This is AI Assistant Clara, Welcome!")