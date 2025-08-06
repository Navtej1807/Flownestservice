import os
import httpx
import json

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def optimize_table_schema(table_schema: str) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"""
You are an expert SQL Database Schema Optimizer.
Given the following table schema, perform these tasks:
1. Analyze the schema and point out any inefficiencies.
2. Recommend schema design improvements.
3. Suggest indexes or normalization strategies if needed.

Table Schema:
{table_schema}

Provide the response in the following JSON format:
{{
  "analysis": "Brief analysis of the current schema",
  "recommendations": "Schema design improvements",
  "indexing_suggestions": "Indexes or normalization strategies"
}}
"""

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=60
        )
        response.raise_for_status()
        result = response.json()

    # Extract model response
    message_content = result["choices"][0]["message"]["content"]

    # Parse JSON response
    try:
        response_dict = json.loads(message_content)
    except json.JSONDecodeError:
        response_dict = {
            "analysis": "Could not parse schema analysis.",
            "recommendations": "Manual review required.",
            "indexing_suggestions": "No suggestions available.",
        }

    return response_dict
