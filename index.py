#import text-to-speech conversion library in Python
import pyttsx3
engine =pyttsx3.init()

#import speech recognition to take commands from user
import speech_recognition as sr

#import wikipedia
import wikipedia

#send mail
import smtplib

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

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com","yourpassword")   #here give your mail id and password
    server.sendmail("abc@gmail.com",to, content)   #your mail id  (this is a dummy value)
    server.close()

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

        elif "send email" in query or "send mail" in query or "send a mail" or "send an email":
            try:
                speak("What do you want me to convey?")
                content = takeCommand()
                to = "xyz@gmail.com"                             #the user's mail id you want to send  (used a dummy here)

                #the next few lines are to send your message to the above user
                #sendmail(to,content)
                #speak("The mail was sent successfully")

                #for now ,we are just speaking the content
                speak(content)
            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "offline" in query or "thank you" in query or "exit" in query:
            quit()
    