import os
import httpx

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def optimize_table_schema(table_schema: str) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"""
You are an SQL Schema Optimization Expert.
Given the following table schema, your task is to:
1. Identify any redundancy or inefficiency.
2. Suggest normalization or denormalization if beneficial.
3. Recommend indexes and partitioning if needed.

Table Schema:
{table_schema}

Provide the response in the following JSON format:
{{
  "issues_found": "Any inefficiencies or redundancy found",
  "optimization_recommendations": "Steps to optimize schema"
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
    import json
    try:
        response_dict = json.loads(message_content)
    except json.JSONDecodeError:
        response_dict = {
            "issues_found": "Could not parse response.",
            "optimization_recommendations": "Manual review required.",
        }

    return response_dict
