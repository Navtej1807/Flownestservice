from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.execution_plan_service import analyze_execution_plan  # ✅ Correct Path

router = APIRouter()

class SQLQuery(BaseModel):
    query: str

@router.post("/")
async def execution_plan(query: SQLQuery):
    try:
        plan = await analyze_execution_plan(query.query)
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
