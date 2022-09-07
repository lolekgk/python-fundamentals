import os
from pathlib import Path

import pytest
from folder_manager import FolderManager


@pytest.fixture
def create_fake_path(fs):
    fs.create_dir('/test/')
    fs.create_dir('/test/x1')
    fs.create_dir('/test/x2')
    fs.create_dir('/test/x3')
    fs.create_dir('/another_test/test1')
    yield fs


@pytest.fixture
def new_path():
    path = Path('/test/test1/test2/test3/test4')
    yield path
    del path


@pytest.fixture
def existing_path():
    path = Path('/another_test/test1')
    yield path
    del path


@pytest.fixture
def main_path():
    path = Path('/test')
    yield path
    del path


@pytest.fixture
def folder_manager():
    fm = FolderManager()
    yield fm
    del fm


class TestFolderManager:
    def test_create_folder_with_new_path(
        self, create_fake_path, new_path, folder_manager
    ):
        folder_manager.create_folder(new_path)
        assert new_path.exists()

    def test_create_folder_with_existing_path(
        self, create_fake_path, existing_path, folder_manager
    ):
        folder_manager.create_folder(existing_path)
        assert existing_path.exists()

    def test_list_content(self, create_fake_path, main_path, folder_manager):
        result = folder_manager.list_content(main_path)
        assert result == ['x1', 'x2', 'x3']

    def test_delete_not_empty_folder_with_ignore_flag(
        self, create_fake_path, main_path, folder_manager
    ):
        folder_manager.delete_folder(main_path, ignore_dir_content=True)
        assert not main_path.exists()

    def test_delete_not_empty_folder_without_ignore_flag(
        self, create_fake_path, main_path, folder_manager
    ):
        with pytest.raises(OSError):
            folder_manager.delete_folder(main_path)

    def test_delete_empty_folder(
        self, create_fake_path, existing_path, folder_manager
    ):
        folder_manager.delete_folder(existing_path)
        assert not existing_path.exists()
