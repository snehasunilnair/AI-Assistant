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
    speak("Cpu is at " + usage + "percent")

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

        elif " daily quote" in query or "quote of the day" in query or "quote" in query:
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
        
        elif "how are you" in query or "how have you been" in query:
            speak("I am doing great! thanks for asking!")
        
        elif "what are you doing" in query or "what are you up to" in query:
            speak("talking to you")

        #to play videos in youtube    
        elif "youtube" in query or "song" in query or "songs" in query:
            if "song" in query or "songs" in query:
                speak("What song would you like to hear?")
            else:
                speak("What would you like to watch?")
            yt_cmd = takeCommand()
            speak('playing' + yt_cmd)
            pywhatkit.playonyt(yt_cmd)

        elif "weather" in query:
            os.system("explorer bingweather:")

        elif "launch" in query or "run" in query or "open" in query or "run" in query:
            if "atom" in query:
                os.system("atom")
            elif "visual studio" in query or "vscode" in query or "visual studio code" in query:
                os.system("code .")
            elif "notepad" in query or "text editor" in query:
                os.system("notepad")
            elif "paint" in query or "mspaint" in query or "draw" in query:
                os.system("Mspaint")
            elif "word" in query or "word doc" in query:
                os.system("start winword")
            elif "excel" in query:
                os.system("start excel")
            elif "powerpoint" in query or "ppt" in query:
                os.system("start powerpnt") 
            
            #social handles
            elif "facebook" in query or "fb" in query:
                os.system("start chrome https://www.facebook.com/")
            elif "instagram" in query or "ig" in query:
                os.system("start chrome https://www.instagram.com/")
            elif "whatsapp web" in query:
                os.system("start chrome https://web.whatsapp.com/")
            elif "twitter" in query:
                os.system("start chrome https://twitter.com/")
            elif "linkedin" in query:
                os.system("start chrome https://www.linkedin.com/")
            elif "medium" in query:
                os.system("start chrome https://medium.com/")

            elif "github" in query:
                os.system("start chrome https://github.com/")
            elif "stack overflow" in query:
                 speak("I see a coder there, keep it up my friend!")
                 os.system("start chrome https://stackoverflow.com/")

            elif "gmeet" in query or "google meet" in query:
                os.system("start chrome https://meet.google.com/") 
            elif "discord" in query:
                os.system("start chrome https://discord.com/") 
            elif "spotify" in query:
                os.system("start chrome https://open.spotify.com/")
            elif "mail" in query or "gmail" in query:
                os.system("start chrome https://mail.google.com/")

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
        