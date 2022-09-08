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

    def create_folder_tree(self, path: Path, tree: dict):
        """Create folder tree in your OS based on provided tree argument of
        dictionary type.
        Example tree structure:
        example_tree = {'name': 'test2', 'type': 'folder', 'content': [{}, {}]}"""
        self._is_valid_tree(tree)
        if tree['type'] == 'folder':
            path = path / tree['name']
        if isinstance(tree.get('content'), list):
            for item in tree['content']:
                if item['type'] == 'folder':
                    self.create_folder_tree(path, item)
        self.create_folder(path)

    def path_to_dict(self, path: Path) -> dict:
        """Create dict representing directory structure in given path"""
        tree = {'name': path.name}
        if path.is_dir():
            tree['type'] = 'folder'
            tree['content'] = [
                self.path_to_dict(item) for item in path.iterdir()
            ]
        if path.is_file():
            tree['type'] = 'file'
        return tree

    def _is_valid_tree(self, tree):
        if not isinstance(tree, dict):
            raise TypeError('You need to provide tree of dict type.')
        if not all(
            item in tree.keys() for item in ['name', 'type', 'content']
        ):
            raise ValueError('You need to provide valid tree structure.')
        if tree.get('content'):
            for item in tree['content']:
                if item.get('type') == 'folder':
                    self._is_valid_tree(item)


tree = {
    'name': 'example',
    'type': 'folder',
    'content': [
        {
            'name': 'subfolder_1',
            'type': 'folder',
            'content': [
                {'name': 'subfolder_1_1', 'type': 'folder', 'content': []},
                {'name': 'subfolder_1_2', 'type': 'folder', 'content': []},
            ],
        },
        {
            'name': 'subfolder_2',
            'type': 'folder',
            'content': [{'name': 'test_file_3.txt', 'type': 'file'}],
        },
    ],
}

# fm = FolderManager()
# path = Path('11241')
# fm._is_valid_tree(tree)
