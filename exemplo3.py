import speech_recognition as sr
import os

recogn = sr.Recognizer()
mic = sr.Microphone()

with mic:
    recogn.adjust_for_ambient_noise(mic, duration=1)
    print("Deseja abrir a agenda?")

    audio = recogn.listen(mic)
    resp = recogn.recognize_google(audio, language='pt')

    if "sim" in resp:
        os.system("C:/Users/logonrmlocal/Desktop/agenda.txt")
    else:
        print("Ok! Encerrando...")
