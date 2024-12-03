import datetime
import logging
from typing import Optional, Union
from fastapi import APIRouter, Depends, HTTPException, Header, status
from jwt import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel
from datetime import datetime as dt


from dependencies import checkToken, getDBHelpr
from utils.Common import Token
from utils.DatabaseHelper import User, DBHelper

router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends()],
    responses={404: {"description": "Not found"}},
)


class LoginRequestUsername(BaseModel):
    username: str
    password: str


class LoginRequestEmail(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


@router.post("/login")
async def login(request: Union[LoginRequestEmail, LoginRequestUsername], DBHelper: DBHelper = Depends(getDBHelpr)):

    __flag = 1  # 1 usrname | 0 email
    if hasattr(request, 'email'):
        email = request.email
        password = request.password
    else:
        __flag = 0
        username = request.username
        password = request.password

    if (__flag):
        try:
            user: User = DBHelper.select(User, email=email)[0]
            payload = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
            if password == user.password:
                return {"accessToken": Token.createToken(payload),
                        "refreshToken": Token.createToken(
                            payload,
                            expires=datetime.timedelta(
                                days=Token.REFRESH_TOKEN_EXPIRE_DAYS),
                            secret_key=Token.REFRESH_KEY
                )}
            else:
                return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="passwd incorrect")
        except IndexError as e:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user not found"+format(e))
        except Exception as e:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=format(e))
    else:
        try:
            user: User = DBHelper.select(User, username=username)[0]
            payload = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
            if password == user.password:
                return {"accessToken": Token.createToken(payload),
                        "refreshToken": Token.createToken(
                            payload,
                            expires=datetime.timedelta(
                                days=Token.REFRESH_TOKEN_EXPIRE_DAYS),
                            secret_key=Token.REFRESH_KEY
                )}
            else:
                return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="passwd incorrect")
        except IndexError as e:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user not found "+format(e))
        except Exception as e:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=format(e))


@router.post("/refresh")
async def refresh(refreshToken: str = Header()):
    if not refresh:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="need refreshToken")
    try:
        payload = Token.verifyToken(
            refreshToken, secret_key=Token.REFRESH_KEY)[1]
        return {
            "accessToken": Token.createToken(payload)
        }
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Expired refreshToekn")
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid refreshToken")


@router.post("/register")
async def register(request: RegisterRequest, DBHelper: DBHelper = Depends(getDBHelpr)):
    __newUser = User(username=request.username,
                     email=request.email,
                     password=request.password,
                     created_at=datetime.datetime.now(datetime.UTC))
    try:
        DBHelper.insert(__newUser)
        return {"status_code": 200}
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/me")
async def getInfo(payload: checkToken = Depends(checkToken), dbHelper: DBHelper = Depends(getDBHelpr)):
    _user_id = payload["id"]
    user_me: User = dbHelper.select(User, id=_user_id)[0]
    user_me.password = "FFFFFFFFFF"
    return user_me
