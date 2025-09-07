from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse
from models.movie import Movie, MovieUpdate, MovieCreate


app = FastAPI()

app.title = "Nuevo titulo"
app.version = "0.0.1"

movies: list[Movie] = []  

@app.get("/", tags=["Home"])
def home():
    return "home"

@app.get("/movies", tags=["Movies"])
def get_movie()-> list[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={"detail": "Movie not found"}, status_code=404)
   

@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int)-> Movie:
    for movie in movies:
        if movie ['category'] == category:
            content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)
    

@app.post("/movies", tags=["Movies"])
def create_movie(movie: MovieCreate) -> list[Movie]:
    movies.append(movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)

@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> list[Movie]:
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.overview = movie.overview
            item.year = movie.year
            item.category = movie.category
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)

@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int) -> list[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
            return JSONResponse(content={"message": "Se elimino la pelicula"})
            
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)
