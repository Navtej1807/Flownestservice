from pydantic import BaseModel

class ExecutionPlanRequest(BaseModel):
    query: str
