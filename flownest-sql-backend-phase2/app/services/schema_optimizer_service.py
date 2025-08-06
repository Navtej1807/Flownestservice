import os
import httpx

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def optimize_schema(schema_description: str) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"""
You are a Database Schema Optimization Assistant.
Given the following schema description, perform the following:
1. Suggest improvements in normalization or indexing.
2. Highlight any redundant columns or tables.
3. Provide optimized schema recommendations.

Schema Description:
{schema_description}

Provide the response in the following JSON format:
{{
  "issues_found": "List of schema design problems",
  "optimization_suggestions": "Recommendations for schema optimization"
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
            "issues_found": "Could not parse model response.",
            "optimization_suggestions": "Manual review required.",
        }

    return response_dict
