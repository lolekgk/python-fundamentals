import shutil
import tempfile
from enum import Enum
from os import name as os_name
from pathlib import Path

from py7zr import pack_7zarchive, unpack_7zarchive


def get_os():
    return os_name


class ArchiveFormat(Enum):
    WINDOWS = '7zip'
    POSIX = 'gztar'


class ArchiveMixin:
    @staticmethod
    def _get_archive_format():

        archive_format = ArchiveFormat.POSIX.value
        if get_os() == 'nt':
            archive_format = ArchiveFormat.WINDOWS.value
            shutil.register_archive_format(
                '7zip',
                pack_7zarchive,
                description='7zip archive',
            )
            shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)
        return archive_format

    def add_files_to_archive(
        self,
        src: Path,
        dst: Path,
        depth: int = -1,
        archive_format: str = _get_archive_format(),
    ):
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
        archive_format: str = _get_archive_format(),
    ):
        with tempfile.TemporaryDirectory() as tmpdir:
            shutil.copytree(src, tmpdir, dirs_exist_ok=True)
            shutil.make_archive(dst, archive_format, tmpdir)
