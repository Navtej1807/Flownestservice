import os
import speech_recognition as sr
from gtts import gTTS
import requests
from dotenv import load_dotenv

load_dotenv()

# ⛓️ Load Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 🎙️ Step 1 - Listen from Mic
def listen_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    print("🧠 Converting speech to text...")
    return recognizer.recognize_google(audio)

# 🤖 Step 2 - Get AI response
def get_gpt_reply(user_input):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }
    res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    return res.json()["choices"][0]["message"]["content"]

# 🔈 Step 3 - Convert Text to Voice
def speak(text):
    tts = gTTS(text=text, lang='en', tld='co.in')
    tts.save("gpt_response.mp3")
    os.system("afplay gpt_response.mp3")

# 🔁 Run
while True:
    try:
        user_text = listen_from_mic()
        print(f"💬 You: {user_text}")
        reply = get_gpt_reply(user_text)
        print(f"🤖 AI: {reply}")
        speak(reply)
        print("🔁 Say something else or press Ctrl+C to exit...\n")
    except KeyboardInterrupt:
        print("\n👋 Exiting. Goodbye!")
        break
    except Exception as e:
        print("⚠️ Error:", e)
