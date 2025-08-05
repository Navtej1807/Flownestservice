from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import httpx
from dotenv import load_dotenv

# Load .env file in local dev (ignored in production on Render)
load_dotenv()

app = FastAPI(title="Flownest SQL Optimizer", version="2.0")

# Fetch API Keys from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
ENTERPRISE_OPTIMIZER_API = os.getenv("ENTERPRISE_OPTIMIZER_API")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not set in environment.")

# === Request & Response Models ===
class SQLRequest(BaseModel):
    query: str

class PlanRequest(BaseModel):
    execution_plan: str

class SchemaRequest(BaseModel):
    schema_design: str

# === Endpoints ===

@app.get("/")
def root():
    return {"message": "Flownest SQL Optimizer API"}

@app.post("/tune-sql")
async def tune_sql(req: SQLRequest):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a SQL query optimization assistant."},
            {"role": "user", "content": f"Optimize this SQL query:\n{req.query}"}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to optimize query via OpenRouter API")
        data = response.json()
        return {"optimized_query": data["choices"][0]["message"]["content"]}

@app.post("/analyze-plan")
async def analyze_execution_plan(req: PlanRequest):
    if not ENTERPRISE_OPTIMIZER_API:
        raise HTTPException(status_code=403, detail="Enterprise API Key not configured for Execution Plan Analyzer")

    # Dummy Logic (Replace with actual API call or custom analysis)
    return {"analysis": f"Execution Plan Analysis of: {req.execution_plan}"}

@app.post("/optimize-schema")
async def optimize_schema(req: SchemaRequest):
    if not ENTERPRISE_OPTIMIZER_API:
        raise HTTPException(status_code=403, detail="Enterprise API Key not configured for Schema Optimizer")

    # Dummy Logic (Replace with actual API call or custom optimization)
    return {"optimized_schema": f"Optimized Schema Design for: {req.schema_design}"}

