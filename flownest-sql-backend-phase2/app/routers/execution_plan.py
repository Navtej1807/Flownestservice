from fastapi import APIRouter, HTTPException
from app.schemas.execution_schema import ExecutionPlanRequest, ExecutionPlanResponse
import requests
import os

router = APIRouter()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@router.post("/execution-plan/", response_model=ExecutionPlanResponse)
def execution_plan(request: ExecutionPlanRequest):
    try:
        prompt = f"Generate an execution plan for the following SQL query and provide recommendations:\n\n{request.sql_query}"
        
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

        return ExecutionPlanResponse(
            execution_plan=ai_output,
            recommendations="AI-generated recommendations"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
