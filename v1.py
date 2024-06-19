from fastapi import FastAPI

app = FastAPI()

data = {
    'id': 1,
    'user_id': 1,
    'title': 'hello world fastapi',
    'body': 'my first fastapi build book api'
}


@app.get('/')
async def book():
    return {'name': "hello world"}


@app.get('/book')
async def datas():
    return data
