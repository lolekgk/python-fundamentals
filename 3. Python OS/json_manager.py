import json


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class JsonManager(metaclass=Singleton):
    def __init__(self, path=None):
        self.path = path

    def read_file(self, path=None):
        # json.load() -> load data from a file
        with open(path) as json_file:
            self.data = json.load(json_file)

    def create_file(self, data: dict):
        # json.dump() -> write data to a file
        with open(self.path, 'w') as json_file:
            json.dump(data, json_file)

    def update_file(self, path):
        # json.load()
        # json.dump()
        pass

    def delete_file(self, path):
        pass


# jsonstring = '{"name": "erik", "age": 38, "married": true}'
# data = json.loads(jsonstring) -> decoding JSON -> json to python, dict
# json.dumps(data, indent=4) -> encoding JSON -> python to json
