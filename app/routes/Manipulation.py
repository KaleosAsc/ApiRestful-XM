from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.get("/")
def Consult_Agent():
    return [{"id": 1, "name": "Juan"}, {"id": 2, "name": "María"}]

@router.post("/")
def Consult_Database(user: User):
    return {"mensaje": f"Usuario {user.name} creado con éxito"}
