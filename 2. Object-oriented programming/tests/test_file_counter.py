from pathlib import Path

import pytest
from file_counter import FileCounter


@pytest.fixture
def extensive_fake_path(fs):
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
def file_counter():
    f = FileCounter()
    yield f
    del f


class TestFileCounter:
    # fs is fixture from pyfakefs library

    def test_file_counter_with_extensive_path(
        self, extensive_fake_path, file_counter
    ):
        path = Path('/test')
        result = file_counter.file_counter(path)
        assert result['files'] == 7
        assert result['folders'] == 5
        assert isinstance(result['results'], dict)
