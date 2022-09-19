import os
import shutil
from enum import Enum
from pathlib import Path

from py7zr import pack_7zarchive


class ArchiveFormat(Enum):
    WINDOWS = '7zip'
    POSIX = 'gztar'


class ArchiveMixin:
    if os.name == 'nt':
        _archive_format = ArchiveFormat.WINDOWS.value
        shutil.register_archive_format(
            ArchiveFormat.WINDOWS.value,
            pack_7zarchive,
            description='7zip archive',
        )
        shutil.register_unpack_format(
            ArchiveFormat.WINDOWS.value, ['.7z'], unpack_7zarchive
        )
    else:
        _archive_format = ArchiveFormat.POSIX.value

    def prepare_files_to_archive(
        self, path: Path, destination: Path, depth: int = -1
    ):
        Path.mkdir(destination)
        for file in self.scan_folder(path, depth):
            try:
                shutil.copy2(file, destination)
            except shutil.SameFileError:
                pass

    def add_to_archive(
        self,
        archive_name: Path,
        root_dir: Path,
        archive_format=_archive_format,
    ):
        shutil.make_archive(archive_name, archive_format, root_dir)

        # try:
        #     shutil.rmtree(root_dir, ignore_errors=True)
        # except OSError as error:
        #     print(error)
