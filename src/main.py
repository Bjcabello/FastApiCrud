from fastapi import FastAPI
from src.routes.movie_router import router

app = FastAPI()

app.title = "Mi Crud de peliculas"
app.version = "0.0.1"

app.include_router(router)