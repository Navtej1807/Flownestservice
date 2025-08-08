# app/schemas/schema_schema.py
from pydantic import BaseModel
from typing import List, Optional

class TableSchema(BaseModel):
    table_name: str
    columns: List[str]
    primary_keys: Optional[List[str]] = None
    indexes: Optional[List[str]] = None

class SchemaRequest(BaseModel):  # <- renamed
    schema_description: str
    tables: List[TableSchema]

class SchemaResponse(BaseModel):  # <- renamed
    suggestions: str
