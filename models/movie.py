from pydantic import BaseModel
from typing import Optional, List

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    category: str


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    overview: Optional[str] = None
    year: Optional[int] = None
    category: Optional[str] = None  