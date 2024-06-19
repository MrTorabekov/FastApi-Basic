from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: int


data = {
    'id': 1,
    'user_id': 1,
    'title': 'hello world fastapi',
    'body': 'my first fastapi build book api'
}
