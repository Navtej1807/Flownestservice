from pydantic import BaseModel

class PlanOptimizationRequest(BaseModel):
    execution_plan: str  # Raw execution plan text

class PlanOptimizationResponse(BaseModel):
    suggestions: str
