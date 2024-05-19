import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import keyboard
from MyAutomations import ChromeAuto,YouTubeAuto,WindiowsAuto,GoogleMaps,Notepad,CloseNotepad
from MyFeatures import GoogleSearch,My_Location,OpenApps,Music

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',180)

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

    return data.lower()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Aarya Sir. Please tell me how may I help you ??")

def speak(audio):
    engine.say(audio)
    print(f' {audio}')
    engine.runAndWait()

Assisstant_info = {'name' : "You should already know that , beacuse you called me just now",
                   'yourself': "I am an voice assistant designed for the B I T Tech Fest",
                   'more about' : "I am designed by the team 'On The Face' of IT First Year",
                    'version' : "I am just a prototype version 1.0"}

Assisstant_info_Hindi = {'नाम' : "आपको यह पहले से ही पता होना चाहिए, क्योंकि आपने मुझे अभी-अभी बुलाया है",
                   'अपने': "मैं एक एआई वॉयस असिस्टेंट हूं जिसे बी आई टी टेक फेस्ट के लिए डिज़ाइन किया गया है",
                   'और जानकारी' : "मुझे आईटी फर्स्ट ईयर की टीम 'ऑन द फेस' द्वारा डिजाइन किया गया है",
                    'वर्जन' : "मैं सिर्फ एक प्रोटोटाइप वर्जन 1.0 हूं"}

if __name__ == "__main__":

    wishMe()
    
    while True:

        command = takeCommand().lower()

        if 'hello' in command:
            speak("Hello Sir , I am arya .")
            speak("Your personal AI Assistant!")
            speak("How May I help you")

        elif 'how are you' in command:
            speak("I Am Fine Sir!")
            speak("What's About You ?")

        elif 'you need a break' in command:
            speak("Ok Sir , You Can Call Me Anytime !")
            speak("Thank You !!")
            speak("Closing....")
            break

        elif 'kya hal hai' in command:
            speak("Mai Badhiya Hoon Aap Batao !!")

        elif 'change language' in command:
            speak("Sir , now we can talk in Hindi !!")
            from HindiMain import HindiTask
            HindiTask()

        elif 'google search' in command:
            from MyFeatures import GoogleSearch
            GoogleSearch()

        elif 'search on youtube' in command:
            speak(" OK Sir , This Is What I Found For Your Search !")
            command = command.replace("search on","")
            command = command.replace("ok","")
            command = command.replace("arya","")
            command = command.replace("youtube","")
            web = 'https://www.youtube.com/results?search_query=' + command
            webbrowser.open(web)
            speak("Done Sir !")
        
        elif 'search on google' in command:
            speak(" OK Sir , This Is What I Found For Your Search !")
            command = command.replace("search on","")
            command = command.replace("arya",'')
            command = command.replace("ok",'')
            command = command.replace("google","")
            pywhatkit.search(command)
            speak("Done Sir !")

        elif 'website' in command:
            speak("Tell Me The Name Of The Website !")
            name = takeCommand().lower()
            
            if 'none' in name:
                speak("No name found !!")
                takeCommand()
            else:
                speak(" OK Sir , Launching.....")
                if 'makaut' in name:
                    webbrowser.open("www.makautexam.net")
                    speak("Done Sir !")
                else:
                    name = name.replace(" ",'')
                    web = 'https://www.' + name + '.com'
                    webbrowser.open(web)
                    speak("Done Sir !")

        elif 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace('wikipedia','')
            command = command.replace('on','')
            command = command.replace('arya','')
            command = command.replace('ok','')
            command = command.replace('search','')
            command = command.replace('show','')
            results = wikipedia.search(f'{command}',suggestion=True)
            results = wikipedia.summary(f'{command}', sentences=2)
            speak("According to Wikipedia ... \n")
            speak(results)

        elif 'music' in command:
            Music()

        elif 'open code' in command:
            OpenApps('code')

        elif 'open word' in command:
            OpenApps('word')

        elif 'open excel' in command:
            OpenApps('excel')

        elif 'open chrome' in command:
            OpenApps('chrome')

        elif 'open edge' in command:
            OpenApps('edge')

        elif 'automate windows' in command:
            speak("What Is Your Command ?")
            from MyAutomations import WindiowsAuto
            command = takeCommand()
            WindiowsAuto(command)

        elif 'where is' in command:
            from MyAutomations import GoogleMaps
            Place = command.replace("where is ","")
            Place = Place.replace("arya" , "")
            GoogleMaps(Place)

        elif 'take me' in command:
            from MyAutomations import GoogleMaps
            Place = command.replace("take me to ","")
            Place = Place.replace("arya" , "")
            GoogleMaps(Place)

        elif 'pause' in command:
            keyboard.press_and_release('space bar')

        elif 'play' in command:
            keyboard.press_and_release('space bar')

        elif 'start video' in command:
            keyboard.press_and_release('0')
    
        elif 'mute' in command:
            keyboard.press_and_release('m')

        elif 'skip' in command:
            keyboard.press_and_release('l')
    
        elif 'back' in command:
            keyboard.press_and_release('j')
    
        elif 'full screen' in command:
            keyboard.press_and_release('f')

        elif 'mini screen' in command:
            keyboard.press_and_release('esc')
    
        elif 'film mode' in command:
            keyboard.press_and_release('t')

        elif 'skip ad' in command:
            keyboard.press_and_release("tab + enter")

        elif 'next' in command:
            keyboard.press_and_release("shift + n")

        elif 'previous' in command:
            keyboard.press_and_release("shift + p")

        elif 'open youtube' in command:
            webbrowser.open("https:\\www.youtube.com")

        elif 'stop' in command:
            keyboard.press_and_release('k')

        elif 'chrome automation' in command:
            speak("What is your command ?")
            comm = takeCommand()
            ChromeAuto(comm)

        elif 'close' in command:
            keyboard.press_and_release('alt + F4')

        elif 'youtube automation' in command:
            YouTubeAuto()

        elif 'remove this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
        
        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

        elif 'joke' in command:
            get = pyjokes.get_joke()
            speak(get)

        elif 'home screen' in command:
            keyboard.press_and_release('windows + m')

        elif 'minimise' in command:
            keyboard.press_and_release('windows + m')

        elif 'show start' in command:
            keyboard.press('windows')

        elif 'open setting' in command:
            keyboard.press_and_release('windows + i')

        elif 'open search' in command:
            keyboard.press_and_release('windows + s')

        elif 'close search' in command:
            keyboard.press_and_release('alt + f4')

        elif 'screenshot' in command:
            keyboard.press_and_release('windows + PrtScn')

        elif 'restore Windows' in  command:
            keyboard.press_and_release('Windows + Shift + M')

        elif 'repeat my words' in command:
            speak("Yes Sir , Tell Me !")
            repeat = takeCommand()
            speak(f'You Said : {repeat}')

        elif 'my location' in command:
            speak("OK Sir , Wait A Second !" )
            My_Location()

        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open facebook' in command:
            webbrowser.open("facebook.com")

        elif 'date' in command:
            strTime = datetime.datetime.now().strftime("%A %m %Y")
            speak(f'Sir, the date is {strTime}')

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')
            print(strTime)

        elif 'shutdown' in command:
            os.system("shutdown /s /t 1")

        elif 'restart' in command:
            os.system("shutdown /r /t 1")

        elif 'sleep' in command:
            os.system("shutdown -l")

        elif 'write a note' in command:
            Notepad()

        elif 'dismiss notepad' in command:
            CloseNotepad()

        elif 'exit arya' in command:
            speak('Ok Sir , You Can Call Me Anytime !')
            speak('Thankyou !!')
            speak('Closing...')
            break
    
        elif 'your name' in command:
            results = Assisstant_info['name']
            speak(results)

        elif 'more about' in command:
            results = Assisstant_info['more about']
            speak(results)
            
        elif 'yourself' in command:
            results = Assisstant_info['yourself']
            speak(results)

        elif 'version' in command:
            results = Assisstant_info['version']
            speak(results)

        elif 'none' in command:
            takeCommand()

        else:

            from ChatBot import ChatterBot

            reply = ChatterBot(command)
            reply = str(reply)

            if 'None' in reply:
                takeCommand()
            else:
                speak(reply)

            if 'bye' in command:
                speak("Closing....")
                break

            elif 'exit' in command:
                speak("Closing....")
                break

            elif 'go' in command:
                speak("Closing....")
                break
