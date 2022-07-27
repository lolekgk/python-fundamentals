from find_in_list import find_item


class TestFindInList:
    def test_find_item_with_one_key_in_list_of_str(self):
        result = find_item(['one', 'two'], 'tw')
        for item in result:
            assert item.value == 'two'
            assert item.index == 1

    def test_find_item_with_many_keys_in_list_of_str(self):
        result = find_item(['one', 'eleven', 'twelve', 'elf'], 'el')
        *_, last_item = result
        assert len(result) == 3
        assert last_item.value == 'elf'
        assert last_item.index == 3

    def test_find_item_with_one_key_in_list_of_non_str(self):
        result = find_item([1, 2, 3, True], 1)
        for item in result:
            assert item.value == 1
            assert item.index == 0

    def test_find_item_with_many_keys_in_list_of_non_str(self):
        result = find_item([11, 22, 33, 41, 26, 101], 1)
        *_, last_item = result
        assert len(result) == 3
        assert last_item.value == 101
        assert last_item.index == 5

    def test_find_item_without_key_in_list(self):
        result = find_item([1, 2, 3], 4)
        assert isinstance(result, tuple)
        assert len(result) == 0
