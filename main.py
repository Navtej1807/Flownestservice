from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SQLQuery(BaseModel):
    query: str

@app.post("/optimize-sql")
def optimize_sql(query: SQLQuery):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return {"error": "API key not found in environment variables"}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are an AI SQL expert. Optimize SQL queries."
            },
            {
                "role": "user",
                "content": f"Optimize this SQL query and explain briefly: {query.query}"
            }
        ]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code != 200:
        return {"error": f"Failed to get response: {response.text}"}

    result = response.json()
    reply = result['choices'][0]['message']['content']
    return {"optimized_query": reply}
