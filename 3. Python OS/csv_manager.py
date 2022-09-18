from __future__ import annotations

import csv
import inspect
import os
from pathlib import Path
from typing import Generator

from pathvalidate import validate_filename


class PathError(Exception):
    def __init__(
        self,
        msg='You need to provide valid path with .csv file to perform this action',
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


class CSVManager(metaclass=Singleton):
    _allowed_extension = '.csv'

    def __init__(self, path: Path = None):
        self.path = path

    def _check_path(func):
        def wrapper(self, *args, **kwargs):

            bound_args = inspect.signature(func).bind(self, *args, **kwargs)
            bound_args.apply_defaults()
            func_args = dict(bound_args.arguments)
            if func_args['path'] is None:
                func_args['path'] = self.path
                return func(*func_args.values())
            return func(*func_args.values())

        return wrapper

    @_check_path
    def read(self, path: Path = None):
        self._is_valid_csv_file_path(path)
        with open(path, newline='', encoding='unicode_escape') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                print(' '.join(row))

    @_check_path
    def write(
        self,
        rows: list[dict],
        header: list[str] = None,
        path: Path = None,
        update: bool = False,
    ) -> CSVManager:
        """Write to .csv file, create if it is not exist."""
        if not update:
            self._is_valid_csv_suffix(path)
            validate_filename(path.stem)

        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if header:
                writer.writerow(header)
            for row in rows:
                if isinstance(row, dict):
                    writer.writerow(list(row.values()))

    @_check_path
    def delete_file(self, path: Path = None) -> CSVManager:
        self._is_valid_csv_file_path(path)
        try:
            os.remove(path)
        except OSError as err:
            print(err)

    @_check_path
    def update_file(self, data: list[dict], path: Path = None) -> CSVManager:
        self.read(path)
        self.write(rows=data, path=path, update=True)

    def scan_folder(self, path: Path = None, depth: int = -1) -> Generator:
        """Recursively list files ending with .csv suffix in all folders in given location
        or up to a certain depth - if provided"""
        self._is_valid_folder_path(path)
        if depth < 0:
            for csv_path in path.rglob(f"*{CSVManager._allowed_extension}"):
                yield csv_path

        if depth >= 0:
            for child in path.iterdir():
                if (
                    child.is_file()
                    and child.suffix == CSVManager._allowed_extension
                ):
                    yield child
                if child.is_dir() and depth > 0:
                    yield from self.scan_folder(child, depth - 1)

    def _is_valid_csv_file_path(self, path: Path):
        if not (
            isinstance(path, Path)
            and path.exists()
            and path.is_file()
            and path.suffix == CSVManager._allowed_extension
        ):
            raise PathError

    def _is_valid_csv_suffix(self, path: Path):
        if (
            not isinstance(path, Path)
            or not path.suffix == CSVManager._allowed_extension
        ):
            raise PathError

    def _is_valid_folder_path(self, path: Path):
        if not isinstance(path, Path) or not path.is_dir():
            raise PathError(
                'You need to provide valid directory path to perform this action.'
            )

    @property
    def allowed_extension(self):
        return self._allowed_extension

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, path: Path):
        if path is not None:
            self._is_valid_csv_file_path(path)
        self._path = path
