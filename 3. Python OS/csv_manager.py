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

    def scan_path(self, path: Path = None, depth: int = None) -> Generator:
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
