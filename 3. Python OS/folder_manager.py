from __future__ import annotations

import inspect
import os
import shutil
from pathlib import Path

from pydantic import Field, StrictStr
from pydantic.dataclasses import dataclass


@dataclass
class Tree:
    folder_name: StrictStr
    content: list[Tree] = Field(default_factory=list)


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

    def create_folder_tree(self, path: Path, tree: Tree):
        """Create folder tree in your OS based on provided tree argument of
        Tree type."""
        self._is_valid_tree(tree)
        path = path / tree.folder_name
        for item in tree.content:
            self.create_folder_tree(path, item)
        self.create_folder(path)

    def path_to_tree(self, path: Path) -> dict:
        """Create Tree object representing directory structure of given path"""
        tree = Tree(path.folder_name)
        if path.is_dir():
            tree.content = [self.path_to_tree(item) for item in path.iterdir()]
        return tree

    def _is_valid_tree(self, tree):
        if not isinstance(tree, Tree):
            raise TypeError('You need to provide tree of Tree type.')
