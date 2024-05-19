import os
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        data = r.recognize_google(audio, language='en-in')
        print(f'You said : {data}\n')

    except sr.UnknownValueError:
        print("Say that again please...")
        return "None"
    except Exception as e:
        print("Say that again please...")
        return "None"

    return data

while True:

    wake_Up = takeCommand().lower()

    if 'hey arya' in wake_Up:
        os.startfile('D:\\TechFest\\Final\\Assistant.py')
    elif 'wake up arya' in wake_Up:
        os.startfile('D:\\TechFest\\Final\\Assistant.py')
    else:
        takeCommand()
