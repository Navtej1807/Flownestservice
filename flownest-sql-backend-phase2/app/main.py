from fastapi import FastAPI
from app.routers.tune_sql import router as tune_router
from app.routers.execution_plan import router as plan_router
from app.routers.schema_optimizer import router as schema_router

app = FastAPI(
    title="FlownestAI SQL Automation API",
    description="Optimize SQL queries, analyze execution plans, and improve schema design using AI.",
    version="1.0.0"
)

# Register routers with their respective paths
app.include_router(tune_router, prefix="/tune-sql", tags=["SQL Tuning"])
app.include_router(plan_router, prefix="/analyze-plan", tags=["Execution Plan Analysis"])
app.include_router(schema_router, prefix="/schema-optimize", tags=["Schema Optimization"])

@app.get("/")
async def root():
    return {"message": "Welcome to FlownestAI SQL Service API"}
