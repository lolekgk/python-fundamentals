from pathlib import Path


class FileCounter:
    def __init__(self):
        self._files_count: int = 0
        self._dirs_count: int = 0

    def _reset(self):
        "Reset instance attributes to init values"
        self._files_count = 0
        self._dirs_count = 0

    def _create_files_tree(self, path: Path) -> dict:
        dirs, files = [], []
        for item in path.iterdir():
            if item.is_dir():
                self._dirs_count += 1
                dirs.append(self._create_files_tree(item))
            if item.is_file():
                self._files_count += 1
                files.append(item.name)
        return {
            'dir_name': path.name,
            'dirs': dirs,
            'files': files,
        }

    def file_counter(self, path: Path) -> dict:
        self._reset()
        files_tree = self._create_files_tree(path)
        return {
            'files': self._files_count,
            'folders': self._dirs_count,
            'results': files_tree,
        }
