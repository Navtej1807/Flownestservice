from fastapi import APIRouter
from app.schemas.schema_schema import SchemaRequest, SchemaResponse
from app.services.schema_optimizer_service import optimize_table_schema

router = APIRouter()

@router.post("/optimize-schema", response_model=SchemaResponse)
async def optimize_schema(request: SchemaRequest):
    response = await optimize_table_schema(request.table_schema)
    return SchemaResponse(**response)
