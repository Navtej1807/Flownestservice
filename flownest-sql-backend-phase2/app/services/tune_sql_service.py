import os
import httpx
import json

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
import logging

logging.basicConfig(level=logging.INFO)
if not OPENROUTER_API_KEY:
    logging.error("OPENROUTER_API_KEY is not set in the environment!")
else:
    logging.info("✅ OPENROUTER_API_KEY loaded successfully.")

async def optimize_sql_query(input_query: str) -> dict:
    # Debug: Print the API key (check Render logs to verify it's loading)
    print(f"OPENROUTER_API_KEY: {OPENROUTER_API_KEY}")

    if not OPENROUTER_API_KEY:
        return {
            "optimized_query": input_query,
            "explanation": "Missing OpenRouter API key. Please set it in environment variables."
        }

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

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e.response.status_code} - {e.response.text}")
        raise
    except Exception as e:
        print(f"General error during API call: {e}")
        raise

    # Extract model's response content
    message_content = result["choices"][0]["message"]["content"]

    # Try parsing JSON-like response from model
    try:
        response_dict = json.loads(message_content)
    except json.JSONDecodeError:
        response_dict = {
            "optimized_query": input_query,
            "explanation": "The model response could not be parsed. Please review manually.",
        }

    return response_dict
