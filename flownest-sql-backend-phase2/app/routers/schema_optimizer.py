from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.schema_optimizer_service import optimize_table_schema  # ✅ Correct Path

router = APIRouter()

class SchemaRequest(BaseModel):
    schema_details: str

@router.post("/")
async def schema_optimizer(request: SchemaRequest):
    try:
        # Extract schema from request
        table_schema = request.schema_details
        
        # Call service function
        result = await optimize_table_schema(table_schema)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
