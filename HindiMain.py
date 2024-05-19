from multiprocessing.spawn import import_main_path
import pyttsx3
import speech_recognition as sr
import datetime
from googletrans import Translator
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
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
        data = r.recognize_google(audio, language='hi')
        print(f'You said : {data}\n')

    except sr.UnknownValueError:
        print("Say that again please...")
        return "None"
    except Exception as e:
        print("Say that again please...")
        return "None"

    return data

def speak(audio):
    engine.say(audio)
    print(f' {audio}')
    engine.runAndWait()

Assisstant_info = {'नाम' : "आपको यह पहले से ही पता होना चाहिए, क्योंकि आपने मुझे अभी-अभी बुलाया है",
                   'अपने': "मैं एक एआई वॉयस असिस्टेंट हूं जिसे बी आई टी टेक फेस्ट के लिए डिज़ाइन किया गया है",
                   'और जानकारी' : "मुझे आईटी फर्स्ट ईयर की टीम 'ऑन द फेस' द्वारा डिजाइन किया गया है",
                    'वर्जन' : "मैं सिर्फ एक प्रोटोटाइप वर्जन 1.0 हूं"}

def Translate(Text):
    translate = Translator()
    result = translate.translate(Text,dest='hi')
    Text_res = result.text()
    return Text_res

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("शुभ प्रभात !")
    
    elif hour>=12 and hour<18:
        speak("शुभ दोपहर !")
    
    else:
        speak("सुसंध्या !!")

    speak("मैं आर्य: हूँ सर. कृपया मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूं ??")

def HindiTask():

    wishMe()

    while True:

        command = takeCommand().lower()

        if 'हेलो' in command:
            speak("नमस्ते महोदय , मैं आर्य: हूँ .")
            speak("आपका व्यक्तिगत एआई सहायक!")
            speak("मैं आपकी मदद कैसे कर सकता हूं ?")

        elif 'नाम' in command:
                results = Assisstant_info['नाम']
                speak(results)

        elif 'और जानकारी' in command:
                results = Assisstant_info['और जानकारी']
                speak(results)

        elif 'अपने' in command:
                results = Assisstant_info['अपने']
                speak(results)

        elif 'वर्जन' in command:
                results = Assisstant_info['वर्जन']
                speak(results)
                
        elif 'विश्राम' in command:
            speak("ठीक है , सर आप मुझे फिर कभी भी दोबारा बुला सकते हैं")
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[0].id)
            rate = engine.getProperty('rate')
            engine.setProperty('rate',180)
            break
            
