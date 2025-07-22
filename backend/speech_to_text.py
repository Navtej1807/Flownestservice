import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("📝 You said:", text)
except sr.UnknownValueError:
    print("😕 Sorry, could not understand audio.")
except sr.RequestError as e:
    print("🚫 Could not request results; {0}".format(e))
