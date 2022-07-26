from datetime import date

import pytest

from estimate_date_medium import estimate_date
from generate_human_easy import (
    generate_country,
    generate_human,
    generate_phone_number,
)
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

    def test_not_sorted_valid_sides(self):
        assert is_rectangular_triangle(4, 3, 5) == True


class TestEstimateDate:
    def test_estimate_date_in_business_week(self):
        start_date = date(2022, 7, 26)
        estimated_hours = 16
        work_days, end_date = estimate_date(start_date, estimated_hours)
        assert work_days == 2
        assert end_date == date(2022, 7, 28)

    def test_estimate_date_between_holidays(self):
        start_date = date(2022, 10, 31)
        estimated_hours = 15
        work_days, end_date = estimate_date(start_date, estimated_hours)
        assert work_days == 2
        assert end_date == date(2022, 11, 3)

    def test_estimate_date_with_weekend_between(self):
        start_date = date(2022, 7, 29)
        estimated_hours = 25
        work_days, end_date = estimate_date(start_date, estimated_hours)
        assert work_days == 4
        assert end_date == date(2022, 8, 4)

    def test_estimate_date_between_new_year(self):
        start_date = date(2022, 12, 30)
        estimated_hours = 15
        work_days, end_date = estimate_date(start_date, estimated_hours)
        assert work_days == 2
        assert end_date == date(2023, 1, 3)

    def test_estimate_date_with_no_work_days(self):
        start_date = date(2022, 7, 26)
        estimated_hours = 0
        work_days, end_date = estimate_date(start_date, estimated_hours)
        assert work_days == 0
        assert end_date == date(2022, 7, 26)


class TestGenerateHuman:
    def test_generate_phone_number(self):
        result = generate_phone_number()
        assert len(result) == 9
        assert result.isnumeric() == True

    def test_generate_country(self):
        with open('countries.txt', 'r') as f:
            countries = f.read().splitlines()
        assert generate_country().upper() in countries

    def test_generate_human_len(self):
        assert len(generate_human()) == 7

    def test_generate_human_email(self):
        result = generate_human()
        assert result['name'].lower() in result['email']
        assert result['surname'].lower() in result['email']

    def test_generate_human_age(self):
        result = generate_human()
        assert result['age'] in range(18, 86)

    def test_generate_human_return_type(self):
        assert isinstance(generate_human(), dict)
