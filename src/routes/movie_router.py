from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from src.models.movie_model import Movie, MovieCreate, MovieUpdate

router = APIRouter()

movies: list[Movie] = []  

@router.get("/", tags=["Home"])
def home():
    return PlainTextResponse(content="Bienvenido a mi API", status_code=200)

@router.get("/movies", tags=["Movies"])
def get_movie()-> list[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)

@router.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={}, status_code=404)
   

@router.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int)-> Movie:
    for movie in movies:
        if movie ['category'] == category:
            content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=404)
    

@router.post("/movies", tags=["Movies"])
def create_movie(movie: MovieCreate) -> list[Movie]:
    movies.append(movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content,  status_code=201)
    #return RedirectResponse(url="/movies", status_code=303)

@router.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> list[Movie]:
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.overview = movie.overview
            item.year = movie.year
            item.category = movie.category
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)

@router.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int) -> list[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
            return JSONResponse(content={"message": "Se elimino la pelicula"})
            
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content, status_code=200)

# @app.get("/file")
# def get_file():
#     return FileResponse('requirements.txt')