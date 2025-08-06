# Existing SQL Tuner Logic Here
import os
import httpx

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

async def optimize_sql_query(input_query: str) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"""
You are a SQL Optimization Assistant.
Given the following SQL query, your task is to:
1. Optimize it for performance.
2. Explain why the optimization is beneficial.
3. If there are no changes needed, mention that explicitly.

SQL Query:
{input_query}

Provide the response in the following JSON format:
{{
  "optimized_query": "Optimized SQL here",
  "explanation": "Explanation of optimization"
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

    # Extracting model's response
    message_content = result["choices"][0]["message"]["content"]

    # Parsing the JSON-like response text to dictionary
    import json
    try:
        response_dict = json.loads(message_content)
    except json.JSONDecodeError:
        response_dict = {
            "optimized_query": input_query,
            "explanation": "The model response could not be parsed. Please review manually.",
        }

    return response_dict
