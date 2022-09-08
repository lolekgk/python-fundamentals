import os
import shutil
from pathlib import Path


class FolderManager:
    def __init__(self, path: Path = None):
        self.path = path

    def create_folder(self, path: Path = None):
        if path is None:
            path = self.path
        os.makedirs(path, exist_ok=True)

    def list_content(self, path: Path = None) -> list:
        if path is None:
            path = self.path
        return os.listdir(path)

    def delete_folder(
        self, path: Path = None, ignore_dir_content: bool = False
    ):
        if path is None:
            path = self.path

        if len(os.listdir(path)) != 0 and not ignore_dir_content:
            raise OSError(f'Directory in provided path: {path} is not empty!')

        try:
            shutil.rmtree(path, ignore_errors=True)
        except OSError as error:
            print(error)

    def create_folder_tree(self, path, folder_tree: dict):
        """Create folder tree in your OS based on provided tree argument of
        dictionary type.
        Example tree structure:
        example_tree = {'name': 'test2', 'type': 'folder', 'content': [{}, {}]}"""
        if folder_tree['type'] == 'folder':
            path = path / folder_tree['name']
        if isinstance(folder_tree.get('content'), list):
            for item in folder_tree['content']:
                if item['type'] == 'folder':
                    self.create_folder_tree(path, item)
        self.create_folder(path)
