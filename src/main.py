# src/main.py
from fastapi import FastAPI
from src.routes.movie_router import router

app = FastAPI()

app.title = "Nuevo titulo"
app.version = "0.0.1"

app.include_router(router)