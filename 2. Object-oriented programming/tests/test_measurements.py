from math import isclose

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
        assert isclose(temp.to_si(), 306.0388888)

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

    def test_compare_centimeter_and_inch(self):
        cm = Centimeter(25.4)
        inch1 = Inch(10)
        inch2 = Inch(100)
        assert cm == inch1
        assert cm >= inch1
        assert inch2 > cm
        assert cm < inch2
        assert inch1 <= cm
        assert cm != inch2


class TestKilometerAndMile:
    def test_kilometer_creation(self):
        km = Kilometer(100)
        assert km.value == 100
        assert str(km) == '100km'

    def test_mile_creation(self):
        mile = Mile(20)
        assert mile.value == 20
        assert str(mile) == '20mi.'

    def test_kilometer_to_si(self):
        km = Kilometer(24)
        assert km.to_si() == 24000

    def test_mile_to_si(self):
        mile = Mile(100)
        assert mile.to_si() == 160934.4

    def test_convert_kilometer_to_mile(self):
        km = Kilometer(50)
        mile = km.to_mile()
        assert isclose(mile.value, 31.07520198)
        assert isinstance(mile, Mile)

    def test_convert_mile_to_kilometer(self):
        mile = Mile(80)
        km = mile.to_kilometer()
        assert isinstance(km, Kilometer)
        assert km.value == 128.72

    def test_kilometer_miles_comparsion(self):
        mile = Mile(60)
        mile2 = Mile(80)
        km = Kilometer(96.5606)
        assert km == mile
        assert mile2 >= mile
        assert km <= mile
        assert mile != mile2
        assert mile2 > mile
        assert km < mile2


class TestLiterAndGallon:
    def test_liter_creation(self):
        l = Liter(100)
        assert l.value == 100
        assert str(l) == '100l'

    def test_gallon_creation(self):
        gal = Gallon(1)
        assert gal.value == 1
        assert str(gal) == '1gal'

    def test_liter_to_si(self):
        l = Liter(1000)
        assert l.to_si() == 1

    def test_gallon_to_si(self):
        gal = Gallon(1000)
        assert gal.to_si() == 3.7854118

    def test_liter_to_gallon(self):
        l = Liter(1000)
        gal = l.to_gallon()
        assert isinstance(gal, Gallon)
        assert gal.value == 264.2007926023778

    def test_gallon_to_liter(self):
        gal = Gallon(10)
        l = gal.to_liter()
        assert isinstance(l, Liter)
        assert l.value == 37.85

    def test_liters_gallons_comparsion(self):
        l1 = Liter(1.5)
        l2 = Liter(1500)
        gal = Gallon(0.396258)
        assert gal == l1
        assert l2 >= l1
        assert gal <= l1
        assert l1 != l2
        assert l2 > l1
        assert gal < l2


def test_different_types_comparision_greather_than():
    km = Kilometer(50)
    temp = Celsius(20)
    with pytest.raises(TypeError):
        km > temp


def test_different_types_comparision_less_than():
    km = Kilometer(50)
    temp = Celsius(20)
    with pytest.raises(TypeError):
        km < temp


def test_different_types_comparision_equall():
    km = Kilometer(50)
    temp = Celsius(20)
    assert not km == temp


def test_different_types_comparision_not_equall():
    km = Kilometer(50)
    temp = Celsius(20)
    assert km != temp


def test_different_types_comparision_greather_or_equall():
    km = Kilometer(50)
    temp = Celsius(20)
    with pytest.raises(TypeError):
        km >= temp
