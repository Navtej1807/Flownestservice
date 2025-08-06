import os
import httpx

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def generate_execution_plan(input_query: str) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"""
You are an SQL Execution Plan Generator.
Given the following SQL query, your task is to:
1. Generate a hypothetical execution plan.
2. Explain which operations are costly and why.
3. Suggest indexes or schema changes if necessary.

SQL Query:
{input_query}

Provide the response in the following JSON format:
{{
  "execution_plan": "Textual execution plan here",
  "bottlenecks": "Explanation of bottlenecks and costly operations",
  "recommendations": "Indexes or schema recommendations"
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
            "execution_plan": "Could not parse execution plan.",
            "bottlenecks": "Manual review required.",
            "recommendations": "No suggestions available.",
        }

    return response_dict
