from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

# ----- Request Models -----
class SQLTuneRequest(BaseModel):
    query: str

class PlanAnalyzeRequest(BaseModel):
    query: str

class SchemaOptimizeRequest(BaseModel):
    schema: str
    query: str

# ----- Utility Function -----
async def call_openrouter(prompt: str):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="OpenRouter API error")
        return response.json()["choices"][0]["message"]["content"]

# ----- Endpoints -----
@app.post("/tune-sql")
async def tune_sql(request: SQLTuneRequest):
    prompt = f"Optimize this SQL query and explain the changes:\n{request.query}"
    result = await call_openrouter(prompt)
    return {"optimized_query": result}

@app.post("/analyze-plan")
async def analyze_plan(request: PlanAnalyzeRequest):
    prompt = f"Analyze the following SQL execution plan and provide performance insights:\n{request.query}"
    result = await call_openrouter(prompt)
    return {"plan_analysis": result}

@app.post("/optimize-schema")
async def optimize_schema(request: SchemaOptimizeRequest):
    prompt = f"Given this database schema:\n{request.schema}\nOptimize the following query considering indexes, joins, and best practices:\n{request.query}"
    result = await call_openrouter(prompt)
    return {"schema_optimized_query": result}

# ----- Health Check -----
@app.get("/")
def read_root():
    return {"status": "SQL Tuner Phase 2 API is running", "environment": ENVIRONMENT}
