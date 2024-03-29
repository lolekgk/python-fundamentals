from __future__ import annotations

import csv
import os
from pathlib import Path

from pathvalidate import validate_filename

from archive import ArchiveMixin
from utils import PathError, ScanFolderMixin, Singleton, check_path


class CSVManager(ArchiveMixin, ScanFolderMixin, metaclass=Singleton):
    _allowed_extension = '.csv'

    def __init__(self, path: Path = None):
        self.path = path

    @check_path
    def read(self, path: Path = None):
        self._is_valid_csv_file_path(path)
        with open(path, newline='', encoding='unicode_escape') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                print(' '.join(row))

    @check_path
    def write(
        self,
        rows: list[dict],
        header: list[str] = None,
        path: Path = None,
        update: bool = False,
    ) -> CSVManager:
        """Write to .csv file, create if it is not exist."""
        if not update:
            self._is_valid_csv_suffix(path)
            validate_filename(path.stem)

        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if header:
                writer.writerow(header)
            for row in rows:
                if isinstance(row, dict):
                    writer.writerow(list(row.values()))

    @check_path
    def delete_file(self, path: Path = None) -> CSVManager:
        self._is_valid_csv_file_path(path)
        try:
            os.remove(path)
        except OSError as err:
            print(err)

    @check_path
    def update_file(self, data: list[dict], path: Path = None) -> CSVManager:
        self.read(path)
        self.write(rows=data, path=path, update=True)

    def _is_valid_csv_file_path(self, path: Path):
        if not (
            isinstance(path, Path)
            and path.exists()
            and path.is_file()
            and path.suffix == CSVManager._allowed_extension
        ):
            raise PathError

    def _is_valid_csv_suffix(self, path: Path):
        if (
            not isinstance(path, Path)
            or not path.suffix == CSVManager._allowed_extension
        ):
            raise PathError

    def _is_valid_folder_path(self, path: Path):
        if not isinstance(path, Path) or not path.is_dir():
            raise PathError(
                'You need to provide valid directory path to perform this action.'
            )

    @property
    def allowed_extension(self):
        return self._allowed_extension

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, path: Path):
        if path is not None:
            self._is_valid_csv_file_path(path)
        self._path = path
