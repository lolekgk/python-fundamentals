from __future__ import annotations

import json
import os
from pathlib import Path

from pathvalidate import validate_filename

from archive import ArchiveMixin
from utils import PathError, ScanFolderMixin, Singleton, check_path


class JsonManager(ArchiveMixin, ScanFolderMixin, metaclass=Singleton):
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

    def _is_valid_json_file_path(self, path: Path):
        if not (
            isinstance(path, Path)
            and path.exists()
            and path.is_file()
            and path.suffix == JsonManager._allowed_extension
        ):
            raise PathError

    def _is_valid_json_suffix(self, path: Path):
        if (
            not isinstance(path, Path)
            or not path.suffix == JsonManager._allowed_extension
        ):
            raise PathError

    def _is_valid_folder_path(self, path: Path):
        if not isinstance(path, Path) or not path.is_dir():
            raise PathError(
                'You need to provide valid directory path to perform this action.'
            )

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
