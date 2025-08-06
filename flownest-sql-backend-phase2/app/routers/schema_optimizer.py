from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.schema_optimizer_service import optimize_schema  # ✅ Correct Path

router = APIRouter()

class SchemaRequest(BaseModel):
    schema_details: str

@router.post("/")
async def schema_optimizer(request: SchemaRequest):
    try:
        result = await optimize_schema(request.schema_details)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
