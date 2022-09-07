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
        ...


{
    'name': 'test',
    'type': 'folder',
    'content': [
        {
            'name': 'subfolder_1',
            'type': 'folder',
            'content': [
                {'name': 'test_file_1.txt', 'type': 'file'},
                {'name': 'test_file_2.txt', 'type': 'file'},
            ],
        },
        {
            'name': 'subfolder_2',
            'type': 'folder',
            'content': [{'name': 'test_file_3.txt', 'type': 'file'}],
        },
    ],
}
fm = FolderManager()
path = Path('/Users/karolgajda/test/test')
print(fm.list_content(path))
dict = {'folder1': ['child1', 'child2']}
print(len(os.listdir(path)) != 0)
