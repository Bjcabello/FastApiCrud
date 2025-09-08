from fastapi import FastAPI
from src.routes.movie_router import router
from src.utils.htttp_error_handler import HttpErrorHandler

app = FastAPI()
app.add_middleware(HttpErrorHandler)

   
    

app.title = "Mi Crud de peliculas"
app.version = "0.0.1"

app.include_router(router)