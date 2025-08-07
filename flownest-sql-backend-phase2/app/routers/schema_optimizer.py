from fastapi import APIRouter
from app.services.schema_optimize_service import optimize_schema
from app.schemas.schema_schema import SchemaOptimizationRequest

router = APIRouter()

@router.post("/schema-optimize/")
async def schema_optimize_route(request: SchemaOptimizationRequest):
    return await optimize_schema(request.schema_description)
