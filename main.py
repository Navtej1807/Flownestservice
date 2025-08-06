from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

from models.request_models import SQLTuneRequest, PlanAnalyzeRequest, SchemaOptimizeRequest
from services.openrouter_client import call_openrouter
from services.prompt_templates import (
    get_tune_prompt,
    get_plan_analysis_prompt,
    get_schema_optimization_prompt
)
from utils.rate_limiter import check_rate_limit

# Load .env variables
load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

# Health Check Endpoint (For Render)
@app.get("/")
def root():
    return {"message": "SQL Tuner Phase 2 API is running", "environment": ENVIRONMENT}

# Endpoint 1: Tune SQL Query
@app.post("/tune-sql")
async def tune_sql(request: SQLTuneRequest):
    await check_rate_limit()
    prompt = get_tune_prompt(request.query)
    result = await call_openrouter(prompt)
    return {"optimized_query": result}

# Endpoint 2: Analyze Execution Plan
@app.post("/analyze-plan")
async def analyze_plan(request: PlanAnalyzeRequest):
    await check_rate_limit()
    prompt = get_plan_analysis_prompt(request.query)
    result = await call_openrouter(prompt)
    return {"plan_analysis": result}

# Endpoint 3: Optimize Schema + Query
@app.post("/optimize-schema")
async def optimize_schema(request: SchemaOptimizeRequest):
    await check_rate_limit()
    prompt = get_schema_optimization_prompt(request.schema, request.query)
    result = await call_openrouter(prompt)
    return {"schema_optimized_query": result}
