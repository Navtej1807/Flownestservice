from fastapi import APIRouter

router = APIRouter()

@router.post('/tune-sql')
def tune_sql():
    return {'message': 'SQL Tuning API (Phase 1)'}
