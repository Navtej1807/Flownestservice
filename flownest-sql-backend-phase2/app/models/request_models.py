from pydantic import BaseModel

class SQLTuneRequest(BaseModel):
    query: str

class PlanAnalyzeRequest(BaseModel):
    query: str

class SchemaOptimizeRequest(BaseModel):
    schema: str
    query: str
