from datetime import date

from count_days import count_days, date_from


class TestCountDays:
    def test_count_days_from_earlier_to_later_date(self):
        date1, date2 = date(2022, 7, 22), date(2022, 7, 25)
        days_difference = count_days(date1, date2)
        assert days_difference == 3

    def test_count_days_from_later_date_to_earlier(self):
        date1, date2 = date(2022, 7, 22), date(2022, 7, 25)
        days_difference = count_days(date2, date1)
        assert days_difference == 3

    def test_date_from_with_positive_days_number(self):
        start_date = date(2022, 7, 26)
        result_date = date_from(start_date, 50)
        assert result_date == date(2022, 9, 14)

    def test_date_from_with_negative_days_number(self):
        start_date = date(2022, 7, 26)
        result_date = date_from(start_date, -50)
        assert result_date == date(2022, 6, 6)
