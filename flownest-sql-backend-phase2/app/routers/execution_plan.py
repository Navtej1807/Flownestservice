from fastapi import APIRouter, HTTPException
from app.services.execution_plan_service import analyze_execution_plan

router = APIRouter()

@router.post("/analyze-execution-plan")
def execution_plan_endpoint(query: str):
    try:
        result = analyze_execution_plan(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
