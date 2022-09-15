from __future__ import annotations

import inspect
import os
import shutil
from pathlib import Path


class FolderManager:
    def __init__(self, path: Path | None = None):
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
    def create_folder(self, path: Path | None = None):
        os.makedirs(path, exist_ok=True)

    @_check_path
    def list_content(self, path: Path | None = None) -> list:
        return os.listdir(path)

    @_check_path
    def delete_folder(
        self, path: Path | None = None, ignore_dir_content: bool = False
    ):
        if len(os.listdir(path)) != 0 and not ignore_dir_content:
            raise OSError(f'Directory in provided path: {path} is not empty!')

        try:
            shutil.rmtree(path, ignore_errors=True)
        except OSError as error:
            print(error)

    def create_folder_tree(self, path: Path, tree: dict):
        """Create folder tree in your OS based on provided tree argument of
        dict type.
        Example:
        tree = {'name': 'example', 'content': []}
        """
        self._is_valid_tree(tree)
        path = path / tree['name']
        for item in tree['content']:
            self.create_folder_tree(path, item)
        self.create_folder(path)

    def path_to_dict(self, path: Path) -> dict:
        """Create dict representing directory structure of given path"""
        tree = {'name': path.name}
        if path.is_dir():
            tree['content'] = [
                self.path_to_dict(item) for item in path.iterdir()
            ]
        return tree

    def _is_valid_tree(self, tree):
        if not isinstance(tree, dict) or not all(
            item in tree.keys() for item in ['name', 'content']
        ):
            raise Exception

        for item in tree['content']:
            self._is_valid_tree(item)
