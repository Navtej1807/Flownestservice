
from fastapi import FastAPI
from routers import tune_sql, execution_plan, schema_optimizer, admin_stats
from middleware.api_key_auth import api_key_auth_middleware

app = FastAPI()

app.middleware("http")(api_key_auth_middleware)

app.include_router(tune_sql.router)
app.include_router(execution_plan.router)
app.include_router(schema_optimizer.router)
app.include_router(admin_stats.router)

@app.get("/")
def root():
    return {"message": "FlownestAI SQL Tuner Backend - Phase 2 Ready"}
