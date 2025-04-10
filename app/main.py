from fastapi import FastAPI
from app.routes import users

app = FastAPI(title="Mi API RESTful con FastAPI")

# Registrar rutas
app.include_router(users.router, prefix="/users", tags=["Usuarios"])

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a mi API con FastAPI"}
