import os
import shutil
import tempfile
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

    def add_files_to_archive(
        self,
        src: Path,
        dst: Path,
        depth: int = -1,
        archive_format=_archive_format,
    ):

        with tempfile.TemporaryDirectory() as tmpdir:
            for file in self.scan_folder(src, depth):
                shutil.copy2(file, tmpdir)

            shutil.make_archive(
                dst,
                archive_format,
                tmpdir,
            )
