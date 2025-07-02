import speech_recognition as sr

def get_spoken_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your Prompt: ")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except Exception as e:
        return "ERROR_SPEECH_NOT_RECOGNIZED"

'''f=get_spoken_speech()
print(f)'''