
from fastapi import APIRouter, Request, HTTPException
# ✅ Correct:
from app.models.user_usage import get_usage_stats


router = APIRouter()

@router.get("/admin/stats")
def admin_stats(request: Request):
    api_key = request.headers.get("Authorization")
    if api_key != "Admin-Secret-Key":
        raise HTTPException(status_code=403, detail="Forbidden")
    return get_usage_stats()
