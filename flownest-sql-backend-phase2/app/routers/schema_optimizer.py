from fastapi import APIRouter, HTTPException
from app.schemas.schema_schema import SchemaOptimizationRequest, SchemaOptimizationResponse
import requests
import os

router = APIRouter()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@router.post("/optimize-schema/", response_model=SchemaOptimizationResponse)
def optimize_schema(request: SchemaOptimizationRequest):
    try:
        prompt = f"Optimize the following database schema:\nDescription: {request.schema_description}\n\nTables:\n"
        for table in request.tables:
            prompt += f"- Table: {table.table_name}\n  Columns: {', '.join(table.columns)}\n"
            if table.primary_keys:
                prompt += f"  Primary Keys: {', '.join(table.primary_keys)}\n"
            if table.indexes:
                prompt += f"  Indexes: {', '.join(table.indexes)}\n"
            prompt += "\n"
        
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

        return SchemaOptimizationResponse(
            suggestions=ai_output
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
