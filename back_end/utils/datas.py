from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

# SQLAlchemy Base


# Pydantic User model
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True



