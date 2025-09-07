from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
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
    return [movie.model_dump() for movie in movies]

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int)-> Movie:
    for movie in movies:
        if movie ['id'] == id:
            return movie.model_dump()
    return []

@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int)-> Movie:
    for movie in movies:
        if movie ['category'] == category:
            return movie.model_dump()
    return []

@app.post("/movies", tags=["Movies"])
def create_movie(movie: MovieCreate) -> list[Movie]:
    movies.append(movie)
    return [movie.model_dump() for movie in movies]

@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> list[Movie]:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['category'] = movie.category
    return [movie.model_dump() for movie in movies]

@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int)-> list[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return {"message": f"Pelicula '{movie['title']}' eliminada exitosamente"}
    return [movie.model_dump() for movie in movies]
