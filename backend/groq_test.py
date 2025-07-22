import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",  # ✅ Updated model name
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hi, I want to order a pizza."}
    ]
}

response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
response_json = response.json()

print("📦 Raw response from Groq:\n", response_json)

if "choices" in response_json:
    print("🤖 Groq says:", response_json["choices"][0]["message"]["content"])
else:
    print("⚠️ 'choices' key missing in response")
