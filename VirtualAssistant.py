import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)
def speak(audio):
    print('F.R.I.D.A.Y.'+audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I: %M : %p")
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning Sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon Sir")
    elif hour>=18 and hour<24:
        speak("Good night Sir")
    speak("How can i help you")
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print('Tony Stark:'+query)
    except sr.UnknownValueError:
        print('Please repeat or typing the command')
        query=str(input('Your order is: '))
    return query
if __name__ =="__main__":
    welcome()
    while(True):
        query=command().lower()
        if "google" in query:
            speak('What should i search boss?')
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "youtube" in query:
            speak('What should i search boss?')
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        if "open video" in query:
            meme=r"C:\Users\QUOC TRUNG\Videos\Captures\meme.mp4"
            os.startfile(meme)
        if "quit" in query:
            speak("Friday is quitting Sir. Goodbye")
            quit()

