from dataclasses import asdict
from pathlib import Path

import pytest
from folder_manager import FolderManager, Tree


@pytest.fixture
def create_fake_path(fs):
    fs.create_dir('/test/')
    fs.create_dir('/test/x1')
    fs.create_dir('/test/x1/xx1')
    fs.create_dir('/test/x1/xx2')
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


@pytest.fixture
def valid_tree():

    leaf_1_1 = Tree('sub_1_1')
    leaf_1_2 = Tree('sub_1_2')
    leaf_1 = Tree('sub_1', [leaf_1_1, leaf_1_2])
    leaf_2 = Tree('sub_2')
    leaf_3 = Tree('sub_3')
    tree = Tree('example', [leaf_1, leaf_2, leaf_3])
    yield tree
    del (
        leaf_1,
        leaf_1_1,
        leaf_1_2,
        leaf_2,
        leaf_3,
        tree,
    )


@pytest.fixture
def invalid_tree():
    tree = {'test': 'sub_test'}
    yield tree
    del tree


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

    def test_create_folder_tree_with_valid_tree(
        self, create_fake_path, valid_tree, main_path, folder_manager
    ):
        folder_manager.create_folder_tree(main_path, valid_tree)
        assert Path('/test/example/sub_1/sub_1_1').exists()
        assert Path('/test/example/sub_1/sub_1_2').exists()
        assert Path('/test/example/sub_2/').exists()
        assert Path('/test/example/sub_3/').exists()

    def test_create_folder_with_invalid_tree_type(
        self, create_fake_path, main_path, folder_manager
    ):
        with pytest.raises(TypeError):
            folder_manager.create_folder_tree(main_path, 1)

    def test_path_to_dict(self, create_fake_path, main_path, folder_manager):
        result = folder_manager.path_to_tree(main_path)
        assert len(asdict(result)['content']) == 3
        assert asdict(result)['folder_name'] == 'test'
        # test the most nested element
        assert (
            asdict(result)['content'][0]['content'][0]['folder_name'] == 'xx1'
        )
