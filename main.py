from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.post("/optimize")
async def optimize_sql(payload: dict):
    query = payload.get("query")
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are an expert SQL query optimizer. You will receive SQL queries and return optimized versions of them with explanation."},
            {"role": "user", "content": f"Optimize this SQL query: {query}"}
        ]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    result = response.json()
    optimized_response = result['choices'][0]['message']['content']
    return {"optimized_query": optimized_response}

@app.get("/")
def read_root():
    return {"message": "Flownest SQL Tuner API is running"}
