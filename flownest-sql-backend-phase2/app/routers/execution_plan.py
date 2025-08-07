from fastapi import APIRouter
from app.services.execution_plan_service import analyze_execution_plan
from app.schemas.plan_schema import ExecutionPlanRequest

router = APIRouter()

@router.post("/analyze-plan/")
async def analyze_plan_route(request: ExecutionPlanRequest):
    return await analyze_execution_plan(request.execution_plan)
