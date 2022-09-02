from pathlib import Path


class PathError(Exception):
    def __init__(
        self,
        msg="You need to provide a file_path as Path object, which points to .csv file.",
        *args,
        **kwargs
    ):
        super().__init__(msg, *args, **kwargs)


class FileHandler:
    _allowed_extensions = ['.csv']

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def __enter__(self):
        self.file_obj = self.file_path.open(
            mode='r', encoding='unicode_escape'
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

    def get_row(self):
        return self.file_obj.readline()

    def _path_validation(self, file_path: Path, allowed_extensions: list):
        if not (
            isinstance(file_path, Path)
            and file_path.exists()
            and file_path.is_file()
            and file_path.suffix in allowed_extensions
        ):
            raise PathError

    @property
    def allowed_extensions(self):
        return self._allowed_extensions

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path: Path):
        self._path_validation(path, FileHandler._allowed_extensions)
        self._file_path = path
