from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import checkToken, getDBHelpr
from ..utils.Common import Token
from ..utils.DatabaseHelper import User, DBHelper

router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends()],
    responses={404: {"description": "Not found"}},
)




@router.post("/login")
async def login(username:str,password:str):
    pass

@router.post("/logout")
async def logout():
    pass

@router.post("/register")
async def register():
    pass

@router.get("/me")
async def getInfo(payload:checkToken = Depends(),dbHelper:DBHelper = Depends(getDBHelpr)):
    _user_id = payload["id"]
    user_me:User = dbHelper.select(User,id=_user_id)[0]
    return  user_me