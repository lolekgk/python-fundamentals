import shutil
import tempfile
from ast import Call
from enum import Enum
from os import name as os_name
from pathlib import Path
from typing import Callable

from py7zr import pack_7zarchive


def get_os():
    return os_name


class ArchiveFormat(Enum):
    WINDOWS = '7zip'
    POSIX = 'gztar'


class ArchiveMixin:
    def _set_archive_format(self):
        self.archive_format = ArchiveFormat.POSIX.value
        if get_os() == 'nt':
            self.archive_format = ArchiveFormat.WINDOWS.value

            if self.archive_format not in {
                k: v for k, v in shutil.get_archive_formats()
            }:
                shutil.register_archive_format(
                    '7zip',
                    pack_7zarchive,
                    description='7zip archive',
                )
        return self.archive_format

    def add_files_to_archive(
        self,
        src: Path,
        dst: Path,
        depth: int = -1,
        archive_format: str | Callable = _set_archive_format,
    ):
        if isinstance(archive_format, Callable):
            archive_format = archive_format(self)

        with tempfile.TemporaryDirectory() as tmpdir:
            for file in self.scan_folder(src, depth):
                shutil.copy2(file, tmpdir)

            shutil.make_archive(
                dst,
                archive_format,
                tmpdir,
            )

    def add_tree_to_archive(
        self,
        src: Path,
        dst: Path,
        archive_format: str | Callable = _set_archive_format,
    ):

        if isinstance(archive_format, Callable):
            archive_format = archive_format(self)

        with tempfile.TemporaryDirectory() as tmpdir:
            shutil.copytree(src, tmpdir, dirs_exist_ok=True)
            shutil.make_archive(dst, archive_format, tmpdir)
