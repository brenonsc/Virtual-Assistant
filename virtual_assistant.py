import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import wikipedia
import pyaudio
import webbrowser

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            speak("Desculpe, não entendi")
        except sr.RequestError:
            speak("Desculpe, não há disponibiidade do serviço")
    return said.lower()

def speak(text):
    tts = gTTS(text=text, lang='pt', tld='com.br')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

def respond(text):
    print("Texto ouvido: " + text)
    if 'youtube' in text:
        speak("O que gostaria de pesquisar?")
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Foi isso o que achei de {keyword} no youtube")
    elif 'wikipedia' in text:
        speak("O que deseja buscar na Wikipedia?")
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("De acordo com a Wikipedia")
            print(result)
            speak(result)
    elif 'que horas são' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    elif 'exit' in text:
        speak("Tchau, tchau, até a próxima!")
        exit()

while True:
    print("Estou ouvindo...")
    text = get_audio()
    respond(text)