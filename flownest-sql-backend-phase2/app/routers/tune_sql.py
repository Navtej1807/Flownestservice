from fastapi import APIRouter, HTTPException
from app.schemas.sql_schema import SQLOptimizationRequest, SQLOptimizationResponse
import requests
import os

router = APIRouter()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@router.post("/tune-sql/", response_model=SQLOptimizationResponse)
def tune_sql(request: SQLOptimizationRequest):
    try:
        prompt = f"Optimize the following SQL query for better performance and explain the changes:\n\n{request.sql_query}"
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        data = response.json()

        if "choices" not in data:
            raise HTTPException(status_code=500, detail="OpenRouter API error")

        ai_output = data["choices"][0]["message"]["content"]

        return SQLOptimizationResponse(
            optimized_query=ai_output,
            explanation="AI-generated SQL optimization"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
