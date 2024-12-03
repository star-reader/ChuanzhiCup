from fastapi import Header
from fastapi import HTTPException ,status
from utils.Common import Token
from utils.DatabaseHelper import DBHelper
from jwt import  InvalidTokenError ,ExpiredSignatureError

def checkToken(Authoriztion:str = Header()) -> object:
    if not Authoriztion or Authoriztion is None:
        raise HTTPException(400,"invaild token")
    try:
        payload:object = Token.verifyToken(Authoriztion)[1]
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="expired token")
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid token")


def getDBHelpr()-> DBHelper:

    yield DBHelper()
