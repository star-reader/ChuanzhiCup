from fastapi import FastAPI ,Depends
from pydantic import BaseModel
from dependencies import checkToken

class Message(BaseModel):
    code: int  = 200
    msg: object | None = None
    

class User(BaseModel):
    id: int | None = None
    nick_name: str | None = None
    token: str | None = None
    

app = FastAPI()

@app.post("/api/login")
def loginApi():
    user = User(id=1,nick_name="a")
    return user

@app.get('/')
def root():
    return {"msg": "hi"}

@app.get('/item/{id}')
def read_item(id: int):
    return {"id":id}

@app.post('/api/info',dependencies=[Depends(checkToken)])
def getInfo():
    return {'data':{
        "chart":[]
    }}