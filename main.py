from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse


app = FastAPI()

app.title = "Nuevo titulo"
app.version = "0.0.1"

movies = [{"id": 1, "title": "Avengers", "overview": "Superheroes salvan el mundo", "year": 2012, "category": "accion"},
          {"id": 2, "title": "Avatar", "overview": "extraterrestres", "year": 2009, "category": "aventura"},
          {"id": 3, "title": "Boruto", "overview": "Pelicula del hijo de naruto", "year": 1997, "category": "drama"}]  

@app.get("/", tags=["Home"])
def home():
    return "home"

@app.get("/movies", tags=["Movies"])
def get_movie():
    return movies

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for movie in movies:
        if movie ['id'] == id:
            return movie
    return []

@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie ['category'] == category:
            return movie
    return []

@app.post("/movies", tags=["Movies"])
def create_movie(id: int, title: str , overview: str , year: int , category: str ):
    movies.append({"id": id, "title": title, "overview": overview, "year": year, "category": category})
    return movies

@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, title: str , overview: str , year: int , category: str):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['category'] = category
            return movie
    return {"message": "Pelicula no encontrada"}

@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return {"message": f"Pelicula '{movie['title']}' eliminada exitosamente"}
    return {"message": "Pelicula no encontrada"}
