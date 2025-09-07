from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    category: str

class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=datetime.datetime.now().year, ge=1900)
    category: str = Field(min_length=5, max_length=20)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "mi pelicula",
                "overview": "trata de peliculas",
                "year": 2012,
                "category": "accion"
            }
        }
    }

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    overview: Optional[str] = None
    year: Optional[int] = None
    category: Optional[str] = None  