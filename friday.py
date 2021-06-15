import pyttsx3
import datetime
import webbrowser as wb
import speech_recognition as sr
import os

friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)

def speak(audio):
    print('F.R.I.D.A.Y: '+audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    # I: số giờ
    # M: số phút
    # p: AP hoặc PM
    speak(Time)

def welcome():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good night sir")
    speak("How can I help you?")

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Detour: " +query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query=str(input("Your order is:"))
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "youtube" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "open video" in query:
            video=r"C:\Users\Admin\Documents\League of Legends\Highlights\Kai'sa Pentakill.webm"
            os.startfile(video)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Friday is quitting sir. Goodbye boss")
            quit()
            
