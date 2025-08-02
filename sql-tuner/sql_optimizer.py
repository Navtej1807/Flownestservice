import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Load the OpenRouter API key from .env
api_key = os.getenv("OPENROUTER_API_KEY")

# Create OpenAI client using OpenRouter endpoint
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def optimize_sql(sql_query):
    response = client.chat.completions.create(
        model="mistralai/mixtral-8x7b-instruct",
        messages=[
            {"role": "system", "content": "You are a SQL performance expert. Help improve SQL queries."},
            {"role": "user", "content": f"Optimize this SQL query:\n\n{sql_query}"}
        ]
    )
    return response.choices[0].message.content

# Run it
if __name__ == "__main__":
    sql_text = input("Paste your SQL query:\n")
    result = optimize_sql(sql_text)
    print("\nOptimized SQL:\n")
    print(result)
