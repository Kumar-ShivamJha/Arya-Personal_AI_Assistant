import googletrans
import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import os
import webbrowser as web
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    print(f' {audio}')
    engine.runAndWait()

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

def GoogleSearch():

    speak("What Do You Want me To Search ?")
    query = takeCommand()

    Query = str(query)
    if 'None' in query:
        GoogleSearch()
    else:
        pywhatkit.search(Query)

def My_Location():

    op = "https://www.google.com/maps/place/Bengal+Institute+Of+Technology/@22.5215651,88.4587223,17z/data=!4m12!1m6!3m5!1s0x3a0274a1c0115249:0x975599390971e184!2sBengal+Institute+Of+Technology!8m2!3d22.5215651!4d88.460911!3m4!1s0x3a0274a1c0115249:0x975599390971e184!8m2!3d22.5215651!4d88.460911"

    speak("Checking....")

    web.open(op)

    r = requests.get('https://get.geojs.io/')

    ip_request = requests.get('https://get.geojs.io/v1/ip.json')

    ip_add = ip_request.json()['ip']
    
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_request = requests.get(url)

    geo_data = geo_request.json()
    
    print(geo_data)

    state = geo_data['city']

    country = geo_data['country']

    speak(f"Sir , You Are Now In {state , country} .")

def Music():
    speak("Tell Me The Name Of The Song !")
    musicName = takeCommand().lower()

    if 'bekhayali' in musicName:
        os.startfile('D:\\TechFest\\Final\\Songs\\Bekhayali.mp3')
        speak("Your Song Has Been Started ! , Enjoy Sir !")

    elif 'tujhe kitna chahane lage' in musicName:
        os.startfile('D:\\TechFest\\Final\\Songs\\Tujhe Kitna Chahne Lage.mp3')
        speak("Your Song Has Been Started ! , Enjoy Sir !")

    elif 'tumse bhi zyada' in musicName:
        os.startfile('D:\\TechFest\\Final\\Songs\\Tumse Bhi Zyada.mp3')
        speak("Your Song Has Been Started ! , Enjoy Sir !")

    elif 'pretty little liar' in musicName:
        os.startfile("D:\\TechFest\\Final\\Songs\\pretty little liar.mp3")
        speak("Your Song Has Been Started ! , Enjoy Sir !")

    elif "none" in musicName:
        Music()

    else:
        pywhatkit.playonyt(musicName)
        speak("Your Song Has Been Started ! , Enjoy Sir !")

def OpenApps(command):

    speak("OK Sir , Wait A Second !")
    
    if 'code' in command:
        os.startfile('C:\\Users\\91933\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

    elif 'chrome' in command:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    
    elif 'word' in command:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    
    elif 'excel' in command:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
    
    elif 'edge' in command:
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk")
