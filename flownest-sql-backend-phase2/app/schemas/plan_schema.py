from pydantic import BaseModel

class ExecutionPlanRequest(BaseModel):
    sql_query: str
    database_type: str  # e.g., 'PostgreSQL', 'MySQL', 'SQLite'
    explain_output: str  # raw EXPLAIN/EXPLAIN ANALYZE output

class ExecutionPlanResponse(BaseModel):
    analysis: str
    recommendations: str
