import json
from pathlib import Path

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
def valid_json_path(create_fake_path):
    path = Path('/test/test.json')
    yield path
    del path


@pytest.fixture
def invalid_json_path(create_fake_path):
    path = Path('/test/test.txt')
    yield path
    del path


@pytest.fixture
def non_existing_json_file_path(create_fake_path):
    path = Path('/test/to_create.json')
    yield path
    del path


@pytest.fixture
def json_manager_instance():
    json_manager = JsonManager()
    yield json_manager
    del json_manager
    Singleton._instances.clear()


class TestJsonManager:
    def test_is_json_manager_singleton(self, json_manager_instance):
        json_manager_2 = JsonManager()
        assert json_manager_2 is json_manager_instance
        del json_manager_2

    def test_instance_attribute_validation_invalid_path_type(
        self, json_manager_instance
    ):
        with pytest.raises(PathError):
            json_manager_instance.path = 1

    def test_instance_attribute_validation_invalid_file_suffix(
        self, create_fake_path, json_manager_instance, invalid_json_path
    ):
        with pytest.raises(PathError):
            json_manager_instance.path = invalid_json_path

    def test_read_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        json_manager_instance,
        valid_json_path,
    ):
        result = json_manager_instance.read(valid_json_path)
        assert result == {
            'name': 'test_name',
            'surname': 'test_surname',
            'age': 60,
            'pets': ['dog', 'cat', 'hamster'],
        }

    def test_read_with_valid_path_provided_as_instance_argument(
        self, create_fake_path, json_manager_instance, valid_json_path
    ):
        json_manager_instance.path = valid_json_path
        assert json_manager_instance.read() == {
            'name': 'test_name',
            'surname': 'test_surname',
            'age': 60,
            'pets': ['dog', 'cat', 'hamster'],
        }

    def test_read_with_invalid_path(
        self, create_fake_path, json_manager_instance
    ):
        with pytest.raises(PathError):
            json_manager_instance.read()

    def test_write_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        json_manager_instance,
        non_existing_json_file_path,
    ):
        data = {'new data': 100}
        json_manager_instance.write(data, non_existing_json_file_path)
        assert json_manager_instance.read(non_existing_json_file_path) == data

    def test_write_with_valid_path_provided_as_instance_argument(
        self, create_fake_path, json_manager_instance, valid_json_path
    ):
        data = {'test': [1, 2, 3]}
        json_manager_instance.path = valid_json_path
        json_manager_instance.write(data)
        assert json_manager_instance.read() == data

    def test_write_with_invalid_path_provided(
        self, create_fake_path, json_manager_instance
    ):
        assert (json_manager_instance.path) is None
        with pytest.raises(PathError):
            json_manager_instance.write({'test': 101})

    def test_update_file_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        json_manager_instance,
        valid_json_path,
    ):
        data = {'update': 201}
        json_manager_instance.update_file(data, valid_json_path)
        assert json_manager_instance.read(valid_json_path) == data

    def test_update_file_with_valid_path_provided_as_instance_argument(
        self, create_fake_path, json_manager_instance, valid_json_path
    ):
        data = {'test': 1}
        json_manager_instance.path = valid_json_path
        json_manager_instance.update_file(data)
        assert json_manager_instance.read() == data

    def test_update_file_with_invalid_path_provided(
        self, create_fake_path, json_manager_instance
    ):
        with pytest.raises(PathError):
            data = {'test': 1}
            json_manager_instance.update_file(data)

    def test_delete_file_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        json_manager_instance,
        valid_json_path,
    ):
        json_manager_instance.delete_file(valid_json_path)
        assert not valid_json_path.exists()

    def test_delete_file_with_valid_path_provided_as_instance_argument(
        self,
        create_fake_path,
        json_manager_instance,
        valid_json_path,
    ):
        json_manager_instance.path = valid_json_path
        json_manager_instance.delete_file()
        assert not valid_json_path.exists()

    def test_update_file_with_invalid_path_provided(
        self, create_fake_path, json_manager_instance
    ):
        with pytest.raises(PathError):
            json_manager_instance.delete_file()
