import pytest

from estimate_date_medium import estimate_date
from generate_human_easy import generate_human
from is_in_list_easy import is_in_list
from is_rectangular_triangle_easy import is_rectangular_triangle


class TestIsInList:
    def test_int_list_with_item(self):
        data = [1, 2, 3, 4]
        result = is_in_list(data, 3)
        assert result == True

    def test_int_list_without_item(self):
        data = [1, 2, 4]
        result = is_in_list(data, 3)
        assert result == False

    def test_list_with_str(self):
        data = [1, 2, 3, 'test']
        result = is_in_list(data, 'test')
        assert result == True

    def test_list_without_str(self):
        data = [1, 2, 3, 'test']
        result = is_in_list(data, 'te')
        assert result == False

    def test_list_with_bool_item(self):
        data = [1, 2, 3, 'test', True]
        result = is_in_list(data, True)
        assert result == True


class TestIsRectangularTriangle:
    def test_invalid_rectangular_traingle_sides(self):
        sides = [4, 3, 2]
        result = is_rectangular_triangle(*sides)
        assert result == False

    def test_valid_rectangular_triangle_sides(self):
        sides = [3, 4, 5]
        result = is_rectangular_triangle(*sides)
        assert result == True
