from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"msg": "hi"}

@app.get('/item/{id}')
def read_item(id: int):
    return {"id":id}