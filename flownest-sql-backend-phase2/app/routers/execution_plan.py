
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.execution_plan_service import analyze_execution_plan


router = APIRouter()

class ExecutionPlanRequest(BaseModel):
    plan_text: str

@router.post("/analyze-plan")
def analyze_plan(request: ExecutionPlanRequest):
    try:
        result = analyze_execution_plan(request.plan_text)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
