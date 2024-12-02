from fastapi import Header
from fastapi import HTTPException
from utils.Common import Token
from utils.DatabaseHelper import DBHelper

def checkToken(jwt:str = Header()):
    if not jwt or jwt is None:
        raise HTTPException(400,"invaild token")
    Token.verifyToken(jwt)


def getDBHelpr()-> DBHelper:
    return DBHelper()