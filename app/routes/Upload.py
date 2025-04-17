from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.get("/")
def Upload_Database():
    return [{"id": 1, "name": "Juan"}, {"id": 2, "name": "María"}]