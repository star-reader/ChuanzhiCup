from datetime import timedelta
import datetime
from threading import Lock
from typing import Optional, Set
from fastapi import HTTPException, status
from jwt import encode, decode

import jwt
from logging import warning





class SingletonClass(type):
    _instance = None
    _instance_lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = type.__call__(cls, *args, **kwargs)
        return cls._instance


class Token():
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    KEY = "test"
    ALGORITHM = "HS256"

    @classmethod
    def createToken(cls,payload: dict, secret_key: Optional[str], algorithm: Optional[str], expires: Optional[int]) -> str:
        data_to_encoder = payload.copy()

        if secret_key is None:
            secret_key = cls.KEY

        if algorithm is None:
            algorithm = cls.ALGORITHM

        if expires:
            expires = datetime.utcnow() + expires
        else:
            expires = datetime.utcnow() + timedelta(minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES)
        data_to_encoder.update({"exp": expires})
        jwt_encode: str = encode(data_to_encoder, secret_key, algorithm)
        return jwt_encode
    
    @classmethod
    def verifyToken(cls,jwt_encode: str, secret_key: Optional[str], algorithm: Optional[str]) -> tuple[bool,Optional[object]]:


        if secret_key is None:
            secret_key = cls.KEY

        if algorithm is None:
            algorithm = cls.ALGORITHM

        try:
            payload = decode(jwt_encode, secret_key, algorithms=algorithm)
            return True,payload
        except jwt.InvalidTokenError or jwt.ExpiredSignatureError as e:
            raise  e


