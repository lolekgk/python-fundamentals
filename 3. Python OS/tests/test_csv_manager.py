import csv
from pathlib import Path

import pytest
from csv_manager import CSVManager, PathError, Singleton


@pytest.fixture
def create_fake_path(fs):
    fs.create_file('/test/test.csv')
    with open('/test/test.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['country', 'capitol', 'country_code'])
        writer.writerows(
            [
                ['Poland', 'Warsaw', 'PL'],
                ['France', 'Paris', 'FR'],
                ['Spain', 'Madrid', 'SP'],
            ]
        )
    fs.create_file('/test/test.json')
    fs.create_file('/test/test1/xx1.csv')
    fs.create_file('/test/test2/xx2_1.csv')
    fs.create_file('/test/test2/xx2_2.csv')
    fs.create_file('/test/test2/xx2_3.csv')
    fs.create_file('/test/test2/test2_1/xx2.csv')
    fs.create_file('/test/test2/test2_1/xx2.json')
    fs.create_file('/test/test3/xx3.csv')
    fs.create_file('/test/test3/test3_1/xx3.csv')
    yield fs


@pytest.fixture
def csv_manager():
    csv_manager = CSVManager()
    yield csv_manager
    del csv_manager
    Singleton._instances.clear()


@pytest.fixture
def invalid_csv_path():
    path = Path('/test/test.json')
    yield path
    del path


@pytest.fixture
def valid_csv_path():
    path = Path('/test/test.csv')
    yield path
    del path


@pytest.fixture
def non_existing_csv_path():
    path = Path('/test/to_create.csv')
    yield path
    del path


@pytest.fixture
def main_directory_path():
    path = Path('/test')
    yield path
    del path


class TestCSVManager:
    def test_is_csv_manager_singleton(self, csv_manager):
        csv_manager_2 = CSVManager()
        assert csv_manager_2 is csv_manager
        del csv_manager_2
        Singleton._instances.clear()

    def test_instance_attribute_validation_invalid_path_type(
        self, csv_manager
    ):
        with pytest.raises(PathError):
            csv_manager.path = 1

    def test_instance_attribute_validation_invalid_file_suffix(
        self, create_fake_path, csv_manager, invalid_csv_path
    ):
        with pytest.raises(PathError):
            csv_manager.path = invalid_csv_path

    def test_read_with_valid_path_provided_as_method_argument(
        self, create_fake_path, csv_manager, valid_csv_path, capsys
    ):
        csv_manager.read(valid_csv_path)
        captured = capsys.readouterr()
        assert (
            captured.out
            == 'country,capitol,country_code\nPoland,Warsaw,PL\nFrance,Paris,FR\nSpain,Madrid,SP\n'
        )

    def test_read_with_valid_path_provided_as_instance_argument(
        self, create_fake_path, csv_manager, valid_csv_path, capsys
    ):
        csv_manager.path = valid_csv_path
        csv_manager.read()
        captured = capsys.readouterr()
        assert (
            captured.out
            == 'country,capitol,country_code\nPoland,Warsaw,PL\nFrance,Paris,FR\nSpain,Madrid,SP\n'
        )

    def test_read_with_invalid_path(self, create_fake_path, csv_manager):
        with pytest.raises(PathError):
            csv_manager.read()

    def test_write_with_valid_path_provided_as_method_argument(
        self, create_fake_path, csv_manager, non_existing_csv_path, capsys
    ):
        rows = [
            {
                'country': 'Netherlands',
                'capitol': 'Amsterdam',
                'country_code': 'NL',
            },
            {
                'country': 'Denmark',
                'capitol': 'Kopenhagen',
                'country_code': 'DN',
            },
            {
                'country': 'Finland',
                'capitol': 'Helsinki',
                'country_code': 'FN',
            },
        ]
        header = ['country', 'capitol', 'country_code']
        csv_manager.write(rows, header, non_existing_csv_path)
        csv_manager.read(non_existing_csv_path)
        captured = capsys.readouterr()
        assert (
            captured.out
            == 'country,capitol,country_code\nNetherlands,Amsterdam,NL\nDenmark,Kopenhagen,DN\nFinland,Helsinki,FN\n'
        )
        del rows, header

    def test_write_with_valid_path_provided_as_method_argument_without_header(
        self, create_fake_path, csv_manager, non_existing_csv_path, capsys
    ):
        rows = [
            {
                'country': 'Netherlands',
                'capitol': 'Amsterdam',
                'country_code': 'NL',
            },
            {
                'country': 'Denmark',
                'capitol': 'Kopenhagen',
                'country_code': 'DN',
            },
            {
                'country': 'Finland',
                'capitol': 'Helsinki',
                'country_code': 'FN',
            },
        ]
        csv_manager.write(rows=rows, path=non_existing_csv_path)
        csv_manager.read(non_existing_csv_path)
        captured = capsys.readouterr()
        assert (
            captured.out
            == 'Netherlands,Amsterdam,NL\nDenmark,Kopenhagen,DN\nFinland,Helsinki,FN\n'
        )
        del rows

    def test_write_with_invalid_path_provided(
        self, create_fake_path, csv_manager
    ):
        with pytest.raises(PathError):
            csv_manager.write([{1: 1, 2: 2, 3: 3}])

    def test_update_file_with_valid_path_provided_as_method_argument(
        self, create_fake_path, csv_manager, valid_csv_path, capsys
    ):
        rows = [
            {
                'country': 'USA',
                'capitol': 'Washington',
                'country_code': 'US',
            },
        ]
        csv_manager.update_file(rows, valid_csv_path)
        csv_manager.read(valid_csv_path)
        captured = capsys.readouterr()
        assert (
            captured.out
            == 'country,capitol,country_code\nPoland,Warsaw,PL\nFrance,Paris,FR\nSpain,Madrid,SP\nUSA,Washington,US\n'
        )
        del rows

    def test_update_file_with_invalid_path_provided(
        self, create_fake_path, csv_manager
    ):
        with pytest.raises(PathError):
            data = [{'test': 1}]
            csv_manager.update_file(data)

    def test_delete_file_with_valid_path_provided_as_method_argument(
        self,
        create_fake_path,
        csv_manager,
        valid_csv_path,
    ):
        csv_manager.delete_file(valid_csv_path)
        assert not valid_csv_path.exists()

    def test_delete_file_with_valid_path_provided_as_instance_argument(
        self,
        create_fake_path,
        csv_manager,
        valid_csv_path,
    ):
        csv_manager.path = valid_csv_path
        csv_manager.delete_file()
        assert not valid_csv_path.exists()

    def test_delete_file_with_invalid_path_provided(
        self, create_fake_path, csv_manager
    ):
        with pytest.raises(PathError):
            csv_manager.delete_file()

    def test_scan_path_without_provided_depth(
        self, create_fake_path, csv_manager, main_directory_path
    ):
        result = csv_manager.scan_path(main_directory_path)
        assert next(result).as_posix() == '/test/test.csv'
        assert next(result).as_posix() == '/test/test1/xx1.csv'
        assert next(result).as_posix() == '/test/test2/xx2_1.csv'
        assert next(result).as_posix() == '/test/test2/xx2_2.csv'
        assert next(result).as_posix() == '/test/test2/xx2_3.csv'
        assert next(result).as_posix() == '/test/test2/test2_1/xx2.csv'
        assert next(result).as_posix() == '/test/test3/xx3.csv'
        assert next(result).as_posix() == '/test/test3/test3_1/xx3.csv'
        with pytest.raises(StopIteration):
            next(result)

    def test_scan_path_with_provided_depth_as_2(
        self, create_fake_path, csv_manager, main_directory_path
    ):
        result = csv_manager.scan_path(main_directory_path, 2)
        assert next(result).as_posix() == '/test/test.csv'
        assert next(result).as_posix() == '/test/test1/xx1.csv'
        assert next(result).as_posix() == '/test/test2/xx2_1.csv'
        assert next(result).as_posix() == '/test/test2/xx2_2.csv'
        assert next(result).as_posix() == '/test/test2/xx2_3.csv'
        assert next(result).as_posix() == '/test/test3/xx3.csv'
        with pytest.raises(StopIteration):
            next(result)

    def test_scan_path_with_provided_depth_as_1(
        self, create_fake_path, csv_manager, main_directory_path
    ):
        result = csv_manager.scan_path(main_directory_path, 1)
        assert next(result).as_posix() == '/test/test.csv'
        with pytest.raises(StopIteration):
            next(result)
