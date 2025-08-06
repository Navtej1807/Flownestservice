
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.schema_optimizer_service import optimize_schema

router = APIRouter()

class SchemaRequest(BaseModel):
    schema_text: str

@router.post("/optimize-schema")
def optimize_schema_route(request: SchemaRequest):
    try:
        result = optimize_schema(request.schema_text)
        return {"recommendations": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
