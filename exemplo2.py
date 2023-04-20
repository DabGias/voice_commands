import speech_recognition as sr

recogn = sr.Recognizer()
mic = sr.Microphone()

try:
    recogn.adjust_for_ambient_noise(mic, duration=1)

    print("Fale algo")

    audio = recogn.listen(mic)

    print("Reconhecendo")
    print(recogn.recognize_google(audio, language="pt"))
except:
    print("Não entendi")
