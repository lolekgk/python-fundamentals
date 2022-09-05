import json
import os
from pathlib import Path

from pathvalidate import validate_filename


class PathError(Exception):
    def __init__(
        self,
        msg='You need to provide valid path with .json file.',
        *args,
        **kwargs,
    ):
        super().__init__(msg, *args, **kwargs)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class JsonManager(metaclass=Singleton):
    _allowed_extensions = ['.json']

    def __init__(self, path: Path = None):
        self.path = path

    def read(self, file_path: Path) -> dict:
        self._path_validation(file_path)
        with open(file_path) as json_file:
            return json.load(json_file)

    def write(self, data: dict, path: Path, update=None):
        if update is None:
            validate_filename(path.stem)
            self._suffix_validation(path)

        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return self

    def update_file(self, data: dict, file_path: Path):
        self.read(file_path)
        self.write(data, file_path, update=True)
        return self

    def delete_file(self, file_path: Path):
        self._path_validation(file_path)
        try:
            os.remove(file_path)
        except OSError as er:
            print(er)
        return self

    def _path_validation(self, file_path: Path):
        if not (
            isinstance(file_path, Path)
            and file_path.exists()
            and file_path.is_file()
            and file_path.suffix in JsonManager._allowed_extensions
        ):
            raise PathError

    def _suffix_validation(self, file_path: Path):
        if not file_path.suffix in JsonManager._allowed_extensions:
            raise PathError
