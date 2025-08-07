from pydantic import BaseModel

class TuneSQLRequest(BaseModel):
    sql_query: str

class TuneSQLResponse(BaseModel):
    optimized_sql: str
    explanation: str
