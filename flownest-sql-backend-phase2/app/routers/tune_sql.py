from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.tune_sql_service import optimize_sql_query  # ✅ Correct Path

router = APIRouter()

class SQLQuery(BaseModel):
    query: str

@router.post("/")
async def tune_sql(query: SQLQuery):
    try:
        optimized_query = await optimize_sql_query(query.query)
        return optimized_query
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
