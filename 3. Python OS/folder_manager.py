from __future__ import annotations

import os
import shutil
from pathlib import Path

from utils import check_path


class FolderManager:
    def __init__(self, path: Path | None = None):
        self.path = path

    @check_path
    def create_folder(self, path: Path = None):
        os.makedirs(path, exist_ok=True)

    @check_path
    def list_content(self, path: Path = None) -> list:
        return os.listdir(path)

    @check_path
    def delete_folder(
        self, path: Path = None, ignore_dir_content: bool = False
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
        if not isinstance(tree, dict):
            raise TypeError
        if not all(item in tree.keys() for item in ['name', 'content']):
            raise ValueError

        for item in tree['content']:
            self._is_valid_tree(item)

    # Helper function
    def create_tree(self, folder_name: str) -> dict:
        content = []
        depth = int(
            input(
                f'\nProvide number of folders you want to create in: "{folder_name}"? '
            )
        )
        if depth > 0:
            for num in range(depth):
                sub_name = input(
                    f"\n{folder_name = }\n {num+1}. subfolder name: "
                )
                content.append(self.create_tree(sub_name))

        return {'name': folder_name, 'content': content}
