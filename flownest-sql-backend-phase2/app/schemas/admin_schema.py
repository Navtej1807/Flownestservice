from pydantic import BaseModel

class AdminRequest(BaseModel):
    command: str  # Admin command

class AdminResponse(BaseModel):
    result: str
