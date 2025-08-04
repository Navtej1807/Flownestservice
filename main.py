from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

# Get API Key from Environment Variable
OPENROUTER_API_KEY = os.getenv("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")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

@app.post("/tune")
def tune_sql(request: QueryRequest):
    prompt = f"""You are an expert SQL Performance Engineer. Optimize the following SQL query for better performance and provide only the optimized query in your response:\n\n{request.query}"""

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to get optimized query from OpenRouter.")

    data = response.json()
    optimized_query = data['choices'][0]['message']['content']

    return {"optimized_query": optimized_query}
