import os
from fastapi import HTTPException

# Simple in-memory counter (for testing purposes)
request_counter = 0
RATE_LIMIT = int(os.getenv("RATE_LIMIT", 100))

async def check_rate_limit():
    global request_counter
    request_counter += 1
    if request_counter > RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
