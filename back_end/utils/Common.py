from datetime import timedelta
from threading import Lock
from jwt import encode

ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
    def createToken(data:dict,secret_key:str,algorithm,Op):
        data_to_encoder = data.copy()
        encode_jwt = encode(payload=data,key=secret_key,algorithm=algorithm,)

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

