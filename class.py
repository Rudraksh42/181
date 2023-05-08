from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime
root = Tk()
root.geometry("500x500")

text_speech = pyttsx3.init()

def speak(audio):
    text_speech.say(audio)
    text_speech.runAndWait()

def r_speech():
    speak("How Can I Help You?")
    print("how can i help you")
    recog  = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recog.listen(source)
        voice_data = ""
        try:
            voice_data = recog.recognize_google(audio, language ="en-in" )
        except sr.UnknownValueError:
            print("pls repeat i didn't get you")
            speak("pls repeat i didn't get you")
    print(voice_data)
    responsed(voice_data)
    
def responsed(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    
    if "name"  in voice_data:
        speak("my name is Jarvis")
        print("my name is Jarvis")
        
    if "my" in voice_data:
        speak("your name is Rohan")
        print("your name is Rohan")
    
    if "time" in voice_data:
        speak("current time is ")
        t1 = datetime.now()
        current_time = t1.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "date" in voice_data:
        speak("todays date is ")
        d1 = datetime.today()
        speak(d1)
        print(d1)
    
          
r_speech()
root.mainloop()            
 