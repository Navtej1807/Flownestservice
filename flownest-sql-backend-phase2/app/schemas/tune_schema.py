from pydantic import BaseModel

class SQLTuneRequest(BaseModel):
    sql_query: str  # Changed to sql_query for consistency

class SQLTuneResponse(BaseModel):
    optimized_query: str
    explanation: str
