import json
import zipfile
from pathlib import Path
from unittest.mock import patch

import pytest
from json_manager import JsonManager, PathError, Singleton


@pytest.fixture
def create_fake_path(fs):
    # "fs" is the reference to the fake file system
    data = {
        'name': 'test_name',
        'surname': 'test_surname',
        'age': 60,
        'pets': ['dog', 'cat', 'hamster'],
    }
    fs.create_file('/test/test.json')
    with open('/test/test.json', 'w') as json_file:
        json.dump(data, json_file)

    fs.create_file('/test/test.txt')
    fs.create_file('/test/test1/xx1.json')
    fs.create_file('/test/test2/xx2_1.json')
    fs.create_file('/test/test2/xx2_2.json')
    fs.create_file('/test/test2/xx2_3.json')
    fs.create_file('/test/test2/test2_1/xx2.json')
    fs.create_file('/test/test2/test2_1/xx2.txt')
    fs.create_file('/test/test3/xx3.json')
    fs.create_file('/test/test3/test3_1/xx3.json')
    yield fs


@pytest.fixture
def fake_directory(tmp_path):
    # SetUp fake directory using temporary path
    root_dir = tmp_path / "sub1"
    root_dir.mkdir()
    root_branch1 = root_dir / 'sub1_1'
    root_branch2 = root_dir / 'sub1_2'
    root_branch1.mkdir(), root_branch2.mkdir()
    txt_file = root_dir / 'not_seen.txt'
    file1 = root_dir / 'test1.json'
    file2 = root_branch1 / 'test2.json'
    file3 = root_branch2 / 'test3.json'
    file1.touch(), file2.touch(), file3.touch(), txt_file.touch()
    destination = tmp_path / 'archive'
    yield root_dir, destination


@pytest.fixture
def name_mock(mocker):
    return mocker.patch("archive.get_os", return_value="nt")


@pytest.fixture
def valid_json_path():
    path = Path('/test/test.json')
    yield path
    del path


@pytest.fixture
def invalid_json_path():
    path = Path('/test/test.txt')
    yield path
    del path


@pytest.fixture
def non_existing_json_file_path():
    path = Path('/test/to_create.json')
    yield path
    del path


@pytest.fixture
def directory_path():
    path = Path('/test')
    yield path
    del path


@pytest.fixture
def json_manager():
    json_manager = JsonManager()
    yield json_manager
    del json_manager
    Singleton._instances.clear()


class TestJsonManager:
    def test_is_json_manager_singleton(self, json_manager):
        json_manager_2 = JsonManager()
        assert json_manager_2 is json_manager
        del json_manager_2
        Singleton._instances.clear()

    def test_instance_attribute_validation_invalid_path_type(
        self, json_manager
    ):
        with pytest.raises(PathError):
            json_manager.path = 1

    def test_instance_attribute_validation_invalid_file_suffix(
        self, create_fake_path, json_manager, invalid_json_path
    ):
        with pytest.raises(PathError):
            json_manager.path = invalid_json_path

    def test_read_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        json_manager,
        valid_json_path,
    ):
        result = json_manager.read(valid_json_path)
        assert result == {
            'name': 'test_name',
            'surname': 'test_surname',
            'age': 60,
            'pets': ['dog', 'cat', 'hamster'],
        }

    def test_read_with_valid_path_provided_as_instance_argument(
        self, create_fake_path, json_manager, valid_json_path
    ):
        json_manager.path = valid_json_path
        assert json_manager.read() == {
            'name': 'test_name',
            'surname': 'test_surname',
            'age': 60,
            'pets': ['dog', 'cat', 'hamster'],
        }

    def test_read_with_invalid_path(self, create_fake_path, json_manager):
        with pytest.raises(PathError):
            json_manager.read()

    def test_write_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        json_manager,
        non_existing_json_file_path,
    ):
        data = {'new data': 100}
        json_manager.write(data, non_existing_json_file_path)
        assert json_manager.read(non_existing_json_file_path) == data

    def test_write_with_valid_path_provided_as_instance_argument(
        self, create_fake_path, json_manager, valid_json_path
    ):
        data = {'test': [1, 2, 3]}
        json_manager.path = valid_json_path
        json_manager.write(data)
        assert json_manager.read() == data
        del data

    def test_write_with_invalid_path(self, create_fake_path, json_manager):
        with pytest.raises(PathError):
            json_manager.write({'test': 101})

    def test_update_file_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        json_manager,
        valid_json_path,
    ):
        data = {'update': 201}
        json_manager.update_file(data, valid_json_path)
        assert json_manager.read(valid_json_path) == data
        del data

    def test_update_file_with_valid_path_provided_as_instance_argument(
        self, create_fake_path, json_manager, valid_json_path
    ):
        data = {'test': 1}
        json_manager.path = valid_json_path
        json_manager.update_file(data)
        assert json_manager.read() == data
        del data

    def test_update_file_with_invalid_path(
        self, create_fake_path, json_manager
    ):
        with pytest.raises(PathError):
            data = {'test': 1}
            json_manager.update_file(data)

    def test_delete_file_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        json_manager,
        valid_json_path,
    ):
        json_manager.delete_file(valid_json_path)
        assert not valid_json_path.exists()

    def test_delete_file_with_valid_path_provided_as_instance_argument(
        self,
        create_fake_path,
        json_manager,
        valid_json_path,
    ):
        json_manager.path = valid_json_path
        json_manager.delete_file()
        assert not valid_json_path.exists()

    def test_delete_file_with_invalid_path(
        self, create_fake_path, json_manager
    ):
        with pytest.raises(PathError):
            json_manager.delete_file()

    def test_scan_folder_without_provided_depth(
        self, create_fake_path, json_manager, directory_path
    ):
        result = json_manager.scan_folder(directory_path)
        assert list(result) == [
            Path('/test/test.json'),
            Path('/test/test1/xx1.json'),
            Path('/test/test2/xx2_1.json'),
            Path('/test/test2/xx2_2.json'),
            Path('/test/test2/xx2_3.json'),
            Path('/test/test2/test2_1/xx2.json'),
            Path('/test/test3/xx3.json'),
            Path('/test/test3/test3_1/xx3.json'),
        ]

    def test_scan_folder_with_provided_depth_as_1(
        self, create_fake_path, json_manager, directory_path
    ):
        result = json_manager.scan_folder(directory_path, 1)
        assert list(result) == [
            Path('/test/test.json'),
            Path('/test/test1/xx1.json'),
            Path('/test/test2/xx2_1.json'),
            Path('/test/test2/xx2_2.json'),
            Path('/test/test2/xx2_3.json'),
            Path('/test/test3/xx3.json'),
        ]

    def test_scan_folder_with_provided_depth_as_0(
        self, create_fake_path, json_manager, directory_path
    ):
        result = json_manager.scan_folder(directory_path, 0)
        assert list(result) == [Path('/test/test.json')]

    def test_is_valid_folder(
        self, create_fake_path, json_manager, valid_json_path
    ):
        with pytest.raises(PathError):
            json_manager._is_valid_folder_path(valid_json_path)

        with pytest.raises(PathError):
            json_manager._is_valid_folder_path('/test')

    def test_is_valid_json_suffix(
        self, create_fake_path, json_manager, valid_json_path
    ):
        with pytest.raises(PathError):
            json_manager._is_valid_json_suffix('/path')

        with pytest.raises(PathError):
            json_manager._is_valid_json_suffix(invalid_json_path)

    # @patch('archive.get_os', 'nt')
    def test_add_tree_to_archive_creation_with_default_format(
        self, tmp_path, json_manager, fake_directory, name_mock
    ):
        root_dir, destination = fake_directory
        import archive

        json_manager.add_tree_to_archive(root_dir, destination)
        assert archive.get_os() == 'nt'
        # assert archive.os_name == 'nt'
        assert (tmp_path / 'archive.tar.gz').exists()

    def test_add_tree_to_archive_creation_with_custom_format(
        self, tmp_path, json_manager, fake_directory
    ):
        root_dir, destination = fake_directory
        json_manager.add_tree_to_archive(root_dir, destination, 'zip')
        archive_path = tmp_path / 'archive.zip'
        archive_content = zipfile.ZipFile(archive_path).namelist()
        assert archive_path.exists()
        assert len(archive_content) == 6

    def test_add_files_to_archive_with_custom_format(
        self, tmp_path, json_manager, fake_directory
    ):
        root_dir, destination = fake_directory
        json_manager.add_files_to_archive(
            root_dir, destination, archive_format='zip'
        )
        archive_path = tmp_path / 'archive.zip'
        archive_content = zipfile.ZipFile(archive_path).namelist()

        assert archive_path.exists()
        assert archive_content == ['test1.json', 'test2.json', 'test3.json']
