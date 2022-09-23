import inspect
from pathlib import Path
from typing import Generator


def check_path(func):
    def wrapper(self, *args, **kwargs):

        bound_args = inspect.signature(func).bind(self, *args, **kwargs)
        bound_args.apply_defaults()
        func_args = dict(bound_args.arguments)
        if func_args['path'] is None:
            func_args['path'] = self.path
            return func(*func_args.values())
        return func(*func_args.values())

    return wrapper


class PathError(Exception):
    def __init__(
        self,
        msg='You need to provide valid directory path to perform this action.',
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


class ScanFolderMixin:
    def scan_folder(self, path: Path, depth: int = -1) -> Generator:
        """Recursively list files ending with self._allowed_extension suffix in all folders in given location
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
