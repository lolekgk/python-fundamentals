from tokenize import Single


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class JsonManager(metaclass=Singleton):
    def __init__(self):
        pass

    def create(self):
        pass

    def update_file(self):
        pass

    def delete_file(self):
        pass
