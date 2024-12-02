from fastapi import Header
from fastapi import HTTPException

def checkToken(token:str = Header()):
    if not token or token is None:
        raise HTTPException(400,"invaild token")
    