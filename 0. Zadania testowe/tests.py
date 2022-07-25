import pytest

from estimate_date_medium import estimate_date
from generate_human_easy import generate_human
from is_in_list_easy import is_in_list
from is_rectangular_triangle_easy import is_rectangular_triangle


class TestIsInList:
    def test_int_list_with_item(self):
        assert is_in_list([1, 2, 3, 4], 3) == True

    def test_int_list_without_item(self):
        assert is_in_list([1, 2, 4], 3) == False

    def test_list_with_str(self):
        assert is_in_list([1, 2, 3, 'test'], 'test') == True

    def test_list_without_str(self):
        assert is_in_list([1, 2, 3, 'test'], 'te') == False

    def test_list_with_bool_item(self):
        assert is_in_list([1, 2, 3, 'test', True], True) == True


class TestIsRectangularTriangle:
    def test_invalid_rectangular_traingle_sides(self):
        assert is_rectangular_triangle(4, 3, 2) == False

    def test_valid_rectangular_triangle_sides(self):
        assert is_rectangular_triangle(3, 4, 5) == True
