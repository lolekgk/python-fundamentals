from __future__ import annotations

import csv
import os
from pathlib import Path
from typing import Generator


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

    def read(self, path: Path = None):
        if path is None:
            path = self.path

        with open(path, newline='', encoding='unicode_escape') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                print(' '.join(row))

    def write(
        self, path: Path, rows: list[dict], header: list[str] = None
    ) -> CSVManager:
        if path is None:
            path = self.path

        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if header is not None:
                writer.writerow(header)
            for row in rows:
                if isinstance(row, dict):
                    writer.writerow(list(row.values()))
        return self

    def delete_file(self, path: Path = None) -> CSVManager:
        if path is None:
            path = self.path

        self._csv_path_validation(path)
        try:
            os.remove(path)
        except OSError as err:
            print(err)
        return self

    def scan_path(self, path: Path = None, depth: int = None) -> Generator:
        """Recursively list files ending with .csv suffix in all folders in given location
        or up to a certain depth - if provided"""
        if path is None:
            path = self.path

        if depth is None:
            for csv_path in path.rglob(f"*{CSVManager._allowed_extension}"):
                yield csv_path

        if depth is not None:
            depth -= 1
            for child in path.iterdir():
                if (
                    child.is_file()
                    and child.suffix == CSVManager._allowed_extension
                ):
                    yield child
                if child.is_dir() and depth > 0:
                    yield from self.scan_path(child, depth)

    def _csv_path_validation(self, file_path: Path):
        if not (
            isinstance(file_path, Path)
            and file_path.exists()
            and file_path.is_file()
            and file_path.suffix == CSVManager._allowed_extension
        ):
            raise PathError
