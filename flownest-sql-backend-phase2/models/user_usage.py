
usage_db = {}

USAGE_LIMIT_PER_DAY = 20

def is_key_valid(api_key: str) -> bool:
    return api_key.startswith("sk-or-")

def track_usage(api_key: str) -> bool:
    usage = usage_db.get(api_key, 0)
    if usage >= USAGE_LIMIT_PER_DAY:
        return False
    usage_db[api_key] = usage + 1
    return True

def get_usage_stats():
    return usage_db
