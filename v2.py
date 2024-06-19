from fastapi import FastAPI

app = FastAPI()

users_db = [
    {"id": 1, "role": "admin", "name": "John Doe"},
    {"id": 2, "role": "investor", "name": "Akbar"},
    {"id": 3, "role": "customer", "name": "Jamshid"},
]


@app.get('/user/{userId}')
async def get_users(userId: int):
    return [users for users in users_db if users.get('id') == userId]


book_db = [
    {"id": 1, "author": 3, "title": "The Age of Loneliness: Essays", "create_at": "2021/05/04", "pages": 1400},
    {"id": 2, "author": 2, "title": "Biology of Being Human", "create_at": "2021/04/09", "pages": 1400},
    {"id": 3, "author": 2, "title": "The Gripping Story ", "create_at": "2024/04/04", "pages": 1400},
    {"id": 4, "author": 3, "title": "Coming Home", "create_at": "2020/04/03", "pages": 1400},
    {"id": 5, "author": 2, "title": "Data Since book", "create_at": "2021/04/04", "pages": 1400},
    {"id": 6, "author": 1, "title": "Python cookbook", "create_at": "2024/02/04", "pages": 1400},
    {"id": 7, "author": 2, "title": "Rust book", "create_at": "2024/03/04", "pages": 1400},
    {"id": 8, "author": 3, "title": "Go lang book", "create_at": "2022/04/04", "pages": 1400},
]


@app.get('/books/{bookId}')
async def books(bookId: int):
    return [book for book in book_db if book.get("id") == bookId]


@app.get('/books')
async def books():
    return book_db
