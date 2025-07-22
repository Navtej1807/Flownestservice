import os
import requests
from gtts import gTTS
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_groq_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("Error from Groq API:", response.json())
        return "Sorry, I couldn't process your request."

# Main interaction
user_input = input("💬 You: ")
reply = get_groq_response(user_input)

# Text-to-speech
tts = gTTS(text=reply, lang='en', tld='co.in')  # Indian female accent
tts.save("gpt_reply.mp3")

# Play the audio (macOS)
os.system("afplay gpt_reply.mp3")

print("🤖 AI:", reply)
