from fastapi import FastAPI
from database.db import engine

from database.models import Base
from routes.auth import router as auth_router
from routes.users import router as user_router
from routes.roles import router as role_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="x402-auth",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(role_router)


@app.get("/")
def home():

    return {
        "service": "x402-auth",
        "status": "running"
    }
