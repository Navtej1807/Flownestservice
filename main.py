from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import tune_sql, execution_plan, schema_optimizer, admin_stats

app = FastAPI(
    title="Flownest SQL Tuner API",
    description="Optimize SQL queries, analyze execution plans, and suggest schema improvements using AI.",
    version="2.0.0"
)

# CORS Middleware (Allow All Origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(tune_sql.router, prefix="/tune-sql", tags=["SQL Tuning"])
app.include_router(execution_plan.router, prefix="/analyze-plan", tags=["Execution Plan"])
app.include_router(schema_optimizer.router, prefix="/optimize-schema", tags=["Schema Optimization"])
app.include_router(admin_stats.router, prefix="/admin-stats", tags=["Admin Stats"])

# Health Check Route
@app.get("/")
def read_root():
    return {"message": "Flownest SQL Tuner API is running!"}
