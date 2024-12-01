from threading import Lock

class SingletonClass(type):
    _instance = None
    _instance_lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = type.__call__(cls, *args, **kwargs)
        return cls._instance
