
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from models.user_usage import track_usage, is_key_valid

async def api_key_auth_middleware(request: Request, call_next):
    path = request.url.path
    if path.startswith("/admin/"):
        return await call_next(request)

    api_key = request.headers.get("Authorization")
    if not api_key or not is_key_valid(api_key):
        return Response(content="Unauthorized", status_code=401)

    if not track_usage(api_key):
        return Response(content="Usage Limit Reached", status_code=429)

    response = await call_next(request)
    return response
