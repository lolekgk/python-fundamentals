import pytest
from big_numbers import pretty_display


class TestBigNumbers:
    def test_pretty_display_for_int_dozens(self, capsys):
        pretty_display(10)
        captured = capsys.readouterr()
        assert captured.out == '10\n'

    def test_pretty_display_for_int_hundreds(self, capsys):
        pretty_display(123)
        captured = capsys.readouterr()
        assert captured.out == "123\n"

    def test_pretty_display_for_int_thousends(self, capsys):
        pretty_display(4789)
        captured = capsys.readouterr()
        assert captured.out == '4,789\n'

    def test_pretty_display_for_int_millions(self, capsys):
        pretty_display(672700)
        captured = capsys.readouterr()
        assert captured.out == '672,700\n'

    def test_pretty_display_for_big_int_number(self, capsys):
        pretty_display(23456789012)
        captured = capsys.readouterr()
        assert captured.out == '23,456,789,012\n'

    def test_pretty_display_for_float_argument(self, capsys):
        pretty_display(9999999.2)
        captured = capsys.readouterr()
        assert captured.out == '9,999,999.2\n'
