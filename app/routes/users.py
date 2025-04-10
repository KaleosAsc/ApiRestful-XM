from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.get("/")
def get_users():
    return [{"id": 1, "name": "Juan"}, {"id": 2, "name": "María"}]

@router.post("/")
def create_user(user: User):
    return {"mensaje": f"Usuario {user.name} creado con éxito"}
