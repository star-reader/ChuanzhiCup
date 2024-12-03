from fastapi import Header
from fastapi import HTTPException ,status
from utils.Common import Token
from utils.DatabaseHelper import DBHelper
from jwt import  InvalidTokenError ,ExpiredSignatureError

def checkToken(jwt:str = Header()) -> object:
    if not jwt or jwt is None:
        raise HTTPException(400,"invaild token")
    try:
        payload:object = Token.verifyToken(jwt)[1]
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="expired token")
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid token")


def getDBHelpr()-> DBHelper:

    return DBHelper()
