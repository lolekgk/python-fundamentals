from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Generator

from pathvalidate import validate_filename


class PathError(Exception):
    def __init__(
        self,
        msg='You need to provide valid path with .json file to perform this action.',
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
    _allowed_extension = '.json'

    def __init__(self, path: Path = None):
        self.path = path

    def read(self, file_path: Path = None) -> dict:
        if file_path is None:
            file_path = self.path
        self._json_path_validation(file_path)
        with open(file_path) as json_file:
            return json.load(json_file)

    def write(
        self, data: dict, path: Path = None, update: bool = None
    ) -> JsonManager:
        if path is None:
            path = self.path
        if update is None:
            self._suffix_validation(path)
            validate_filename(path.stem)
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return self

    def update_file(self, data: dict, file_path: Path = None) -> JsonManager:
        if file_path is None:
            file_path = self.path
        self.read(file_path)
        self.write(data, file_path, update=True)
        return self

    def delete_file(self, file_path: Path = None) -> JsonManager:
        if file_path is None:
            file_path = self.path
        self._json_path_validation(file_path)
        try:
            os.remove(file_path)
        except OSError as er:
            print(er)
        return self

    def scan_path(self, path: Path = None, depth: int = None) -> Generator:
        """Recursively list files ending with .json suffix in all folders in given location
        or up to a certain depth - if provided"""
        if path is None:
            path = self.path

        if depth is None:
            for tree_path in path.rglob(f'*{JsonManager._allowed_extension}'):
                yield tree_path

        if depth is not None:
            depth -= 1
            for item in path.iterdir():
                if (
                    item.suffix == JsonManager._allowed_extension
                    and item.is_file()
                ):
                    yield item
                if item.is_dir() and depth > 0:
                    yield from self.scan_path(item, depth)

    def _json_path_validation(self, file_path: Path):
        if not (
            isinstance(file_path, Path)
            and file_path.exists()
            and file_path.is_file()
            and file_path.suffix == JsonManager._allowed_extension
        ):
            raise PathError

    def _suffix_validation(self, file_path: Path):
        if (
            not isinstance(file_path, Path)
            or not file_path.suffix == JsonManager._allowed_extension
        ):
            raise PathError

    @property
    def allowed_extensions(self) -> list:
        return self._allowed_extension

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, path: Path):
        if path is not None:
            self._json_path_validation(path)
        self._path = path
