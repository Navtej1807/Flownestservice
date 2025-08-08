from pydantic import BaseModel
from typing import List, Optional

class TableSchema(BaseModel):
    table_name: str
    columns: List[str]  # List of column names
    primary_keys: Optional[List[str]] = None
    indexes: Optional[List[str]] = None

class SchemaOptimizationRequest(BaseModel):
    schema_description: str
    tables: List[TableSchema]

class SchemaOptimizationResponse(BaseModel):
    suggestions: str
