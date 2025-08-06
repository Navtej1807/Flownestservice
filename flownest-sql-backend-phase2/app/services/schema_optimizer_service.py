from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.schema_optimizer_service import optimize_table_schema  # ✅ Correct Import

router = APIRouter()

class SchemaInput(BaseModel):
    schema_details: str

@router.post("/optimize-schema")
async def optimize_schema_endpoint(input_data: SchemaInput):
    try:
        result = await optimize_table_schema(input_data.schema_details)  # ✅ Correct Function Call
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
