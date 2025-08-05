from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/tune-sql")
def tune_sql(query_input: QueryInput):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not API_KEY:
    raise ValueError("API Key not found. Set OPENROUTER_API_KEY as environment variable.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are an expert SQL Performance Tuner."},
            {"role": "user", "content": f"Optimize this SQL Query: {query_input.query}"}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to get optimized query")

    result = response.json()
    optimized_query = result['choices'][0]['message']['content']

    return {"optimized_query": optimized_query}
