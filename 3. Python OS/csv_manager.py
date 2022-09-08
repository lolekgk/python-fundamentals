import csv
from pathlib import Path
from typing import Generator


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

    def write():
        pass

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
