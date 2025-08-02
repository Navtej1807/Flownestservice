from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from optimizer import optimize_sql

app = FastAPI()

class SQLRequest(BaseModel):
    query: str

@app.post("/optimize")
def optimize(request: SQLRequest):
    try:
        optimized = optimize_sql(request.query)
        return optimized
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
