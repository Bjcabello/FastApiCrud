from fastapi import FastAPI
from routes import movie


app = FastAPI()

app.title = "Nuevo titulo"
app.version = "0.0.1"

app.include_router(movie.router)
