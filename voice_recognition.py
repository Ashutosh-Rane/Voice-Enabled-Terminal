import speech_recognition as sr

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Listening for voice command...]")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("[Error: Could not understand the audio]")
        except sr.RequestError as e:
            print(f"[Error: Could not request results from Google Speech Recognition service; {e}]")
    return None

