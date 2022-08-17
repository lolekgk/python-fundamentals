import pytest
from measurements import (
    Celsius,
    Centimeter,
    Fahrenheit,
    Gallon,
    Inch,
    Kilometer,
    Liter,
    Mile,
)


class TestCelsiusAndFahrenheit:
    def test_celsius_creation(self):
        temp = Celsius(32)
        assert temp.value == 32
        assert str(temp) == '32°C'

    def test_fahrenheit_creation(self):
        temp = Fahrenheit(91.2)
        assert temp.value == 91.2
        assert str(temp) == '91.2°F'

    def test_convert_celsius_to_si(self):
        temp = Celsius(32)
        assert temp.to_si() == 305.15

    def test_convert_fahrenheit_to_si(self):
        temp = Fahrenheit(91.2)
        assert round(temp.to_si(), 2) == 306.04

    def test_convert_celsius_to_fahrenheit(self):
        temp = Celsius(32)
        temp2 = temp.to_fahrenheit()
        assert temp2.value == 89.6
        assert isinstance(temp2, Fahrenheit)

    def test_convert_fahrenheit_to_celsius(self):
        temp = Fahrenheit(89.6)
        temp2 = temp.to_celsius()
        assert temp2.value == 32
        assert isinstance(temp2, Celsius)

    def test_celsius_equall(self):
        temp1 = Celsius(20)
        temp3 = Celsius(20)
        assert temp1 == temp3

    def test_celsius_not_equall(self):
        temp1 = Celsius(20)
        temp2 = Celsius(40)
        assert temp1 != temp2

    def test_celsius_greater_than(self):
        temp1 = Celsius(20)
        temp2 = Celsius(40)
        assert temp2 > temp1

    def test_celsius_less_than(self):
        temp1 = Celsius(20)
        temp2 = Celsius(40)
        assert temp1 < temp2

    def test_celsius_greater_or_equal(self):
        temp1 = Celsius(20)
        temp2 = Celsius(40)
        temp3 = Celsius(40)
        assert temp3 >= temp1
        assert temp2 >= temp3

    def test_celsius_less_or_equal(self):
        temp1 = Celsius(20)
        temp2 = Celsius(40)
        temp3 = Celsius(40)
        assert temp1 <= temp3
        assert temp3 <= temp2


class TestCentimeterAndInch:
    def test_centimeter_creation(self):
        cm = Centimeter(100)
        assert cm.value == 100
        assert str(cm) == '100cm'

    def test_inch_creation(self):
        inch = Inch(10)
        assert inch.value == 10
        assert str(inch) == '10″'

    def test_centimeter_to_si(self):
        cm = Centimeter(90)
        assert cm.to_si() == 0.9

    def test_inch_to_si(self):
        inch = Inch(10)
        assert inch.to_si() == 0.254

    def test_centimeter_to_inch(self):
        cm = Centimeter(2.54)
        inch = cm.to_inch()
        assert isinstance(inch, Inch)
        assert inch.value == 1

    def test_inch_to_centimeter(self):
        inch = Inch(100)
        cm = inch.to_centimeter()
        assert isinstance(cm, Centimeter)
        assert cm.value == 254

    def test_inch_is_equall(self):
        inch1 = Inch(100)
        inch2 = Inch(100)
        assert inch1 == inch2

    def test_inch_not_equall(self):
        inch1 = Inch(110)
        inch2 = Inch(100)
        assert inch1 != inch2

    def test_inch_greater_than(self):
        inch1 = Inch(110)
        inch2 = Inch(100)
        assert inch1 > inch2

    def test_inch_less_than(self):
        inch1 = Inch(110)
        inch2 = Inch(100)
        assert inch2 < inch1

    def test_inch_greater_or_equall(self):
        inch1 = Inch(110)
        inch2 = Inch(100)
        inch3 = Inch(110)
        assert inch1 >= inch2
        assert inch1 >= inch3

    def test_inch_less_or_equall(self):
        inch1 = Inch(110)
        inch2 = Inch(100)
        inch3 = Inch(110)
        assert inch2 <= inch1
        assert inch3 <= inch1
