import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)  # Adjust the speech rate (slower is more affectionate)
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0), 1 is the maximum


def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        # print(time)
        talk('Babu current time is '+ time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is' , '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk("SAKSHAM,  everything is for you")

    elif 'i love u' in command:
        talk("I love you too")
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')
run_alexa()