#import text-to-speech conversion library in Python
import pyttsx3
engine =pyttsx3.init()

#import speech recognition to take commands from user
import speech_recognition as sr

#import wikipedia
import wikipedia

#for quotes
import wikiquote

#make system tell jokes ;-)
import pyjokes

#for playing in youtube
import pywhatkit

#to send mail
import smtplib

#for chrome 
import webbrowser as wb

#system functions
import os

#import date-time library
import datetime

#battery and cpu updates
import psutil

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

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com","yourpassword")   #here give your mail id and password
    server.sendmail("abc@gmail.com",to, content)   #your mail id  (this is a dummy value)
    server.close()

def jokes():
    speak(pyjokes.get_joke())

def cpu():
    usage =str(psutil.cpu_percent())
    speak("Cpu is at " + usage)

def Battery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak("Battery is at" +str((percentage)) +"percent")
    
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

        elif "quote" in query or "quotes" in query:
            speak(wikiquote.quote_of_the_day())

        elif "search in chrome" in query or "chrome search" in query or "google" in query:
            speak("What should i search?")
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chrome_path).open_new_tab(search+ ".com")

        elif "send email" in query or "send mail" in query or "send a mail" in query or "send an email" in query:
            try:
                speak("What do you want me to convey?")
                content = takeCommand()
                to = "xyz@gmail.com"                             #the user's mail id you want to send  (used a dummy here)

                #the commented lines below are to send your message to the above user
                #sendmail(to,content)
                #speak("The mail was sent successfully")

                #for now ,we are just speaking the content
                speak(content)
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        
        #to ask AI to rememeber and store the data in a text file
        elif "remember" in query:
            speak("What should i remember?")
            data=takeCommand()
            speak("You said me to remeber " +data)
            remember = open("data.txt", "w")       #here a text file of data.txt is created which stores the data
            remember.write(data)
            remember.close()

        elif "remind" in query or "reminder" in query:
            remember = open("data.txt", "r")
            speak("you said me to remember that" + remember.read())   #speaks the contents in file data.txt

        elif "joke" in query or "jokes" in query:
            jokes()

        #to play videos in youtube    
        elif "youtube" in query or "song" in query or "songs" in query:
            if "song" in query or "songs" in query:
                speak("What song would you like to hear?")
            else:
                speak("What would you like to watch?")
            yt_cmd = takeCommand()
            speak('playing' + yt_cmd)
            pywhatkit.playonyt(yt_cmd)

        elif "cpu" in query:
            cpu()
        
        elif "battery" in query:
            Battery()
        
        elif "logout" in query:
            os.system("shutdown - l")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "offline" in query or "thank you" in query or "exit" in query:
            quit()
        