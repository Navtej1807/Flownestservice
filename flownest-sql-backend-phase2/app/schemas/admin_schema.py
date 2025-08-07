from pydantic import BaseModel

class AdminStats(BaseModel):
    total_requests: int
    successful_requests: int
    failed_requests: int
    uptime: str
