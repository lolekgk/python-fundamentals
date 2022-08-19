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


@pytest.fixture
def temp_celsius():
    return Celsius(32)


@pytest.fixture
def temp_celsius2():
    return Celsius(40)


@pytest.fixture
def temp_fahrenheit():
    return Fahrenheit(91.2)


@pytest.fixture
def cm():
    return Centimeter(25.4)


@pytest.fixture
def inch():
    return Inch(100)


@pytest.fixture
def mile():
    return Mile(80)


@pytest.fixture
def km():
    return Kilometer(96.5606)


@pytest.fixture
def liter():
    return Liter(1500)


@pytest.fixture
def gal():
    return Gallon(0.396258)


class TestCelsiusAndFahrenheit:
    def test_celsius_type(self, temp_celsius):
        assert temp_celsius.type.value == 'temperature'

    def test_fahrenheit_creation(self, temp_fahrenheit):
        assert temp_fahrenheit.type.value == 'temperature'

    def test_convert_celsius_to_si(self, temp_celsius):
        assert temp_celsius.to_si() == 305.15

    def test_convert_fahrenheit_to_si(self, temp_fahrenheit):
        assert isclose(temp_fahrenheit.to_si(), 306.0388888)

    def test_convert_celsius_to_fahrenheit(self, temp_celsius):
        temp_fahrenheit = temp_celsius.to_fahrenheit()
        assert temp_fahrenheit.value == 89.6
        assert isinstance(temp_fahrenheit, Fahrenheit)

    def test_convert_fahrenheit_to_celsius(self, temp_fahrenheit):
        temp_celsius = temp_fahrenheit.to_celsius()
        assert isclose(temp_celsius.value, 32.888, rel_tol=0.001)
        assert isinstance(temp_celsius, Celsius)

    def test_celsius_equall(self, temp_celsius):
        temp_celsius2 = Celsius(32)
        assert temp_celsius == temp_celsius2

    def test_celsius_not_equall(self, temp_celsius, temp_celsius2):
        assert temp_celsius != temp_celsius2

    def test_celsius_greater_than(self, temp_celsius, temp_celsius2):
        assert temp_celsius2 > temp_celsius

    def test_celsius_less_than(self, temp_celsius, temp_celsius2):
        assert temp_celsius < temp_celsius2

    def test_celsius_greater_or_equal(self, temp_celsius, temp_celsius2):
        temp3 = Celsius(40)
        assert temp3 >= temp_celsius
        assert temp_celsius2 >= temp3

    def test_celsius_less_or_equal(self, temp_celsius, temp_celsius2):

        temp3 = Celsius(40)
        assert temp_celsius <= temp3
        assert temp3 <= temp_celsius2


class TestCentimeterAndInch:
    def test_centimeter_creation(self, cm):
        assert cm.type.value == 'length'

    def test_inch_creation(self, inch):
        assert inch.type.value == 'length'

    def test_centimeter_to_si(self, cm):
        assert cm.to_si() == 0.254

    def test_inch_to_si(self, inch):
        assert inch.to_si() == 2.54

    def test_centimeter_to_inch(self, cm):
        inch = cm.to_inch()
        assert isinstance(inch, Inch)
        assert inch.value == 10

    def test_inch_to_centimeter(self, inch):
        cm = inch.to_centimeter()
        assert isinstance(cm, Centimeter)
        assert cm.value == 254

    def test_compare_centimeter_and_inch(self, inch, cm):
        inch2 = Inch(10)
        assert cm == inch2
        assert cm >= inch2
        assert inch > cm
        assert cm < inch
        assert inch2 <= cm
        assert cm != inch


class TestKilometerAndMile:
    def test_kilometer_creation(self, km):
        assert km.type.value == 'length'

    def test_mile_creation(self, mile):
        assert mile.type.value == 'length'

    def test_kilometer_to_si(self, km):
        assert isclose(km.to_si(), 96560.5, rel_tol=0.0001)

    def test_mile_to_si(self, mile):
        assert mile.to_si() == 128747.52

    def test_convert_kilometer_to_mile(self, km):
        mile = km.to_mile()
        assert mile.value == 60.01280298321939
        assert isinstance(mile, Mile)

    def test_convert_mile_to_kilometer(self, mile):
        km = mile.to_kilometer()
        assert isinstance(km, Kilometer)
        assert km.value == 128.72

    def test_kilometer_miles_comparsion(self, mile, km):
        mile1 = Mile(60)
        assert km == mile1
        assert mile >= mile1
        assert km <= mile1
        assert mile1 != mile
        assert mile > mile1
        assert km < mile


class TestLiterAndGallon:
    def test_liter_creation(self, liter):
        assert liter.type.value == 'volume'

    def test_gallon_creation(self, gal):
        assert gal.type.value == 'volume'

    def test_liter_to_si(self, liter):
        assert liter.to_si() == 1.5

    def test_gallon_to_si(self, gal):
        assert isclose(gal.to_si(), 0.00149, rel_tol=0.01)

    def test_liter_to_gallon(self, liter):
        gal = liter.to_gallon()
        assert isinstance(gal, Gallon)
        assert gal.value == 396.3011889035667

    def test_gallon_to_liter(self, gal):
        l = gal.to_liter()
        assert isinstance(l, Liter)
        assert l.value == 1.49983653

    def test_liters_gallons_comparsion(self, liter, gal):
        l1 = Liter(1.5)
        assert gal == l1
        assert liter >= l1
        assert gal <= l1
        assert l1 != liter
        assert liter > l1
        assert gal < liter


def test_different_types_comparision_greather_than(km, temp_celsius):
    with pytest.raises(TypeError):
        km > temp_celsius


def test_different_types_comparision_less_than(km, temp_celsius):
    with pytest.raises(TypeError):
        km < temp_celsius


def test_different_types_comparision_equall(km, temp_celsius):
    with pytest.raises(TypeError):
        km == temp_celsius


def test_different_types_comparision_not_equall(km, temp_celsius):
    with pytest.raises(TypeError):
        km != temp_celsius


def test_different_types_comparision_greather_or_equall(km, temp_celsius):
    with pytest.raises(TypeError):
        km >= temp_celsius
