from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Generator

from pathvalidate import validate_filename

from archive import ArchiveMixin
from utils import PathError, Singleton, check_path


class JsonManager(ArchiveMixin, metaclass=Singleton):
    _allowed_extension = '.json'

    def __init__(self, path: Path = None):
        self.path = path

    @check_path
    def read(self, path: Path = None) -> dict:
        self._is_valid_json_file_path(path)
        with open(path) as json_file:
            return json.load(json_file)

    @check_path
    def write(
        self, data: dict, path: Path = None, update: bool = False
    ) -> JsonManager:
        """Write to .json file, create if it is not exist."""
        if not update:
            self._is_valid_json_suffix(path)
            validate_filename(path.stem)
        with open(path, 'w') as json_file:
            json.dump(data, json_file)

    @check_path
    def update_file(self, data: dict, path: Path = None) -> JsonManager:
        self.read(path)
        self.write(data, path, update=True)

    @check_path
    def delete_file(self, path: Path = None) -> JsonManager:
        self._is_valid_json_file_path(path)
        try:
            os.remove(path)
        except OSError as er:
            print(er)

    def scan_folder(self, path: Path, depth: int = -1) -> Generator:
        """Recursively list files ending with .json suffix in all folders in given location
        or up to a certain depth - if provided"""
        self._is_valid_folder_path(path)
        if depth < 0:
            for tree_path in path.rglob(f'*{self._allowed_extension}'):
                yield tree_path

        else:
            for item in path.iterdir():
                if item.suffix == self._allowed_extension and item.is_file():
                    yield item
                if item.is_dir() and depth > 0:
                    yield from self.scan_folder(item, depth - 1)

    def _is_valid_json_file_path(self, path: Path):
        if not (
            isinstance(path, Path)
            and path.exists()
            and path.is_file()
            and path.suffix == self._allowed_extension
        ):
            raise PathError(
                'You need to provide valid path to existing file '
                f'with {self._allowed_extension} suffix to perform this action'
            )

    def _is_valid_json_suffix(self, path: Path):
        if (
            not isinstance(path, Path)
            or not path.suffix == self._allowed_extension
        ):
            raise PathError(
                'You need to provide valid path with '
                f'{self._allowed_extension} suffix to perform this action.'
            )

    def _is_valid_folder_path(self, path: Path):
        if not isinstance(path, Path) or not path.is_dir():
            raise PathError

    @property
    def allowed_extension(self) -> list:
        return self._allowed_extension

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, path: Path):
        if path is not None:
            self._is_valid_json_file_path(path)
        self._path = path
