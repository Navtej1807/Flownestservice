from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def optimize_sql(query):
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY not found. Make sure it's set in the environment or .env file.")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://flownest.ai",
        "X-Title": "SQL Tuner"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a senior SQL performance expert. Optimize the user's SQL query and explain the changes."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    # Raise an error if something goes wrong
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
