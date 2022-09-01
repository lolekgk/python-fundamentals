import csv
from pathlib import Path

import pytest
from context_manager import FileHandler, PathError


@pytest.fixture
def create_fake_path_with_csv(fs):
    fs.create_file('/test/test1.csv')
    with open('/test/test1.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['country', 'capitol', 'country_code'])
        writer.writerows(
            [
                ['Poland', 'Warsaw', 'PL'],
                ['Germany', 'Berlin', 'DE'],
                ['Czech Republic', 'Prague', 'CZ'],
            ]
        )
    yield fs


@pytest.fixture
def create_fake_path_with_empty_directory(fs):
    fs.create_dir('/test')
    yield fs


@pytest.fixture
def create_fake_path_with_txt_file(fs):
    fs.create_file('/test/test.txt')
    yield fs


@pytest.fixture
def valid_path_with_csv():
    path = Path('/test/test1.csv')
    yield path
    del path


@pytest.fixture
def valid_path_with_empty_dir():
    path = Path('/test')
    yield path
    del path


@pytest.fixture
def valid_path_with_txt_suffix():
    path = Path('/test/test.txt')
    yield path
    del path


@pytest.fixture
def non_existing_path():
    path = Path('/not_existing/path')
    yield path
    del path


class TestFileHandler:
    def test_get_row_with_valid_path(
        self, create_fake_path_with_csv, valid_path_with_csv
    ):
        with FileHandler(valid_path_with_csv) as file:
            assert file.get_row() == 'country,capitol,country_code\n'
            assert file.get_row() == 'Poland,Warsaw,PL\n'
            assert file.get_row() == 'Germany,Berlin,DE\n'
            assert file.get_row() == 'Czech Republic,Prague,CZ\n'

    def test_get_row_with_empty_directory_path(
        self,
        create_fake_path_with_empty_directory,
        valid_path_with_empty_dir,
    ):
        with pytest.raises(PathError) as exc:
            with FileHandler(valid_path_with_empty_dir) as file:
                file.get_row()
        assert (
            str(exc.value)
            == 'You need to provide a file_path as Path object, which points to .csv file.'
        )

    def test_get_row_with_invalid_path(self):
        with pytest.raises(PathError):
            with FileHandler('invalid path') as file:
                file.get_row()

    def test_get_row_with_valid_path_but_with_txt_file(
        self, create_fake_path_with_txt_file, valid_path_with_txt_suffix
    ):
        with pytest.raises(PathError):
            with FileHandler(valid_path_with_txt_suffix) as file:
                file.get_row()

    def test_get_row_non_existing_path(self, non_existing_path):
        with pytest.raises(PathError):
            with FileHandler(non_existing_path) as file:
                file.get_row()
