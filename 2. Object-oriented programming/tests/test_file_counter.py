from pathlib import Path

import pytest
from file_counter import FileCounter


# fs is fixture from pyfakefs library
@pytest.fixture
def create_extensive_fake_path(fs):
    # "fs" is the reference to the fake file system
    fs.create_file('/test/test1/xx1.txt')
    fs.create_file('/test/test2/xx2_1.txt')
    fs.create_file('/test/test2/xx2_2.txt')
    fs.create_file('/test/test2/xx2_3.txt')
    fs.create_file('/test/test2/test2_1/xx2.txt')
    fs.create_file('/test/test3/xx3.txt')
    fs.create_file('/test/test3/test3_1/xx3.txt')
    yield fs


@pytest.fixture
def create_simple_fake_path(fs):
    fs.create_dir('/test')
    yield fs


@pytest.fixture
def file_counter():
    f = FileCounter()
    yield f
    del f


@pytest.fixture
def path():
    path = Path('/test')
    yield path
    del path


class TestFileCounter:
    def test_file_counter_with_extensive_path(
        self, create_extensive_fake_path, path, file_counter
    ):
        result = file_counter.file_counter(path)
        assert result['files'] == 7
        assert result['folders'] == 5
        assert len(result['results']) == 3

    def test_file_counter_with_simple_path(
        self, create_simple_fake_path, path, file_counter
    ):
        result = file_counter.file_counter(path)
        assert result['files'] == 0
        assert result['folders'] == 0
        assert len(result['results']) == 3

    def test_create_files_tree(
        self, create_extensive_fake_path, path, file_counter
    ):
        result = file_counter.file_counter(path)
        assert len(result['results']['dirs']) == 3
        # test the most nested element
        assert (
            result['results']['dirs'][-1]['dirs'][-1]['files'][-1] == 'xx3.txt'
        )

    def test_reset(self, create_extensive_fake_path, path, file_counter):
        file_counter.file_counter(path)
        file_counter.file_counter(path)
        assert file_counter._files_count == 7
        assert file_counter._dirs_count == 5
