from fastapi import APIRouter, HTTPException
from app.models.user_usage import get_usage_stats  # ✅ Fixed Import Path

router = APIRouter()

@router.get("/admin/stats")
async def admin_stats():
    try:
        usage_data = get_usage_stats()
        return usage_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
