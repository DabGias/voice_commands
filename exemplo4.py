import speech_recognition as sr

recogn = sr.Recognizer()
mic = sr.Microphone()

with mic:
    recogn.adjust_for_ambient_noise(mic, duration=1)
    print("informe a multiplicação...")

    audio = recogn.listen(mic)
    resp = recogn.recognize_google(audio, language='pt')

    print(resp)

    if "+" in resp:
        print("{} = {}".format(resp, int(resp.split(" ")[0]) + int(resp.split(" ")[-1])))
    elif "x" in resp:
        print("{} = {}".format(resp, int(resp.split(" ")[0]) * int(resp.split(" ")[-1])))
    elif "-" in resp:
        print("{} = {}".format(resp, int(resp.split(" ")[0]) - int(resp.split(" ")[-1])))
    elif "/" in resp and int(resp.split(" ")[-1]) != 0:
        print("{} = {}".format(resp, int(resp.split(" ")[0]) - int(resp.split(" ")[-1])))
    elif "elevado a" in resp:
        print("{} = {}".format(resp, int(resp.split(" ")[0]) ** int(resp.split(" ")[-1])))
