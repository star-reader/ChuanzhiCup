from fastapi import APIRouter, Depends
from pydantic import BaseModel

from dependencies import checkToken

router = APIRouter(
    prefix="/items",
    tags=["item"],
    dependencies=[Depends(checkToken)],
    responses={404: {"description": "Not found"}},
)

class ItemAddRequest(BaseModel):
    name:str
    tags:str
    price:int
    description:str
    image:str
    fresh_level:str
    period:str
    ranking:int

@router.get("/{item_id}")
async def getItem():
    pass

@router.post("/update/{item_id}")
async def updateItem(update_key:str,update_value:str):
    pass

@router.post("/add")
async def addItem(item:ItemAddRequest):
    pass