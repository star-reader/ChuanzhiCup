from datetime import timedelta
import datetime
from threading import Lock
from typing import Optional, Set
from fastapi import HTTPException, status
from jwt import encode, decode

import jwt
import logging





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
    REFRESH_TOKEN_EXPIRE_DAYS = 7
    KEY = "aaeb0897f9c1e2eb261e05af473c1345de1dfbe962a85188c30335d038748a51"
    REFRESH_KEY = "a3b61948328733317599379dba5834b610ce4115558b2f7ee740574f12c04967"
    ALGORITHM = "HS256"

    @classmethod
    def createToken(cls,payload: dict, secret_key: Optional[str]= None, algorithm: Optional[str] = None, expires: Optional[int] =None) -> str:
        data_to_encoder = payload.copy()

        if secret_key is None:
            secret_key = cls.KEY

        if algorithm is None:
            algorithm = cls.ALGORITHM

        if expires:
            expires = datetime.datetime.now(datetime.UTC) + expires
        else:
            expires = datetime.datetime.now(datetime.UTC) + timedelta(minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES)
        data_to_encoder.update({"exp": expires})
        jwt_encode: str = encode(data_to_encoder, secret_key, algorithm)
        return jwt_encode
    
    @classmethod
    def verifyToken(cls,jwt_encode: str, secret_key: Optional[str] = None, algorithm: Optional[str] = None) -> tuple[bool,Optional[object]]:


        if secret_key is None:
            secret_key = cls.KEY

        if algorithm is None:
            algorithm = cls.ALGORITHM

        try:
            payload = decode(jwt_encode, secret_key, algorithms=algorithm)
            return True,payload
        except jwt.InvalidTokenError or jwt.ExpiredSignatureError as e:
            raise  e
