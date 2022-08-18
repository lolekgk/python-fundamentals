from abc import ABC, abstractmethod
from math import isclose


class Unit(ABC):
    @property
    @abstractmethod
    def unit_symbol(self):
        pass

    @property
    @abstractmethod
    def quantity(self):
        pass

    @abstractmethod
    def to_si(self):
        pass

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}{self.unit_symbol}'

    def __eq__(self, other):
        if self.quantity == other.quantity:
            return isclose(self.to_si(), other.to_si(), rel_tol=0.00001)
        return NotImplemented

    def __ge__(self, other):
        if self.quantity == other.quantity:
            return (
                isclose(self.to_si(), other.to_si(), rel_tol=0.00001)
                or self.to_si() > other.to_si()
            )
        return NotImplemented

    def __le__(self, other):
        if self.quantity == other.quantity:
            return (
                isclose(self.to_si(), other.to_si(), rel_tol=0.00001)
                or self.to_si() < other.to_si()
            )
        return NotImplemented

    def __gt__(self, other):
        if self.quantity == other.quantity:
            return (
                not isclose(self.to_si(), other.to_si(), rel_tol=0.00001)
                and self.to_si() > other.to_si()
            )
        return NotImplemented

    def __lt__(self, other):
        if self.quantity == other.quantity:
            return (
                not isclose(self.to_si(), other.to_si(), rel_tol=0.00001)
                and self.to_si() < other.to_si()
            )
        return NotImplemented


class Celsius(Unit):
    quantity = 'temperature'
    unit_symbol = '°C'

    def to_si(self):
        return self.value + 273.15

    def to_fahrenheit(self):
        value = self.value * 1.8 + 32
        return Fahrenheit(value)


class Fahrenheit(Unit):
    quantity = 'temperature'
    unit_symbol = '°F'

    def to_si(self):
        return (self.value + 459.67) * 5 / 9

    def to_celsius(self):
        value = (self.value - 32) * 5 / 9
        return Celsius(value)


class Centimeter(Unit):
    quantity = 'length'
    unit_symbol = 'cm'

    def to_si(self):
        return self.value * 0.01

    def to_inch(self):
        value = self.value / 2.54
        return Inch(value)


class Inch(Unit):
    quantity = 'length'
    unit_symbol = '″'

    def to_si(self):
        return self.value * 0.0254

    def to_centimeter(self):
        value = self.value * 2.54
        return Centimeter(value)


class Kilometer(Unit):
    quantity = 'length'
    unit_symbol = 'km'

    def to_si(self):
        return self.value * 1000

    def to_mile(self):
        value = self.value / 1.609
        return Mile(value)


class Mile(Unit):
    quantity = 'length'
    unit_symbol = 'mi.'

    def to_si(self):
        return self.value * 1609.344

    def to_kilometer(self):
        value = self.value * 1.609
        return Kilometer(value)


class Liter(Unit):
    quantity = 'volume'
    unit_symbol = 'l'

    def to_si(self):
        return self.value * 0.001

    def to_gallon(self):
        value = self.value / 3.785
        return Gallon(value)


class Gallon(Unit):
    quantity = 'volume'
    unit_symbol = 'gal'

    def to_si(self):
        return self.value * 0.0037854118

    def to_liter(self):
        value = self.value * 3.785
        return Liter(value)


mile = Mile(60)
print(mile.to_si())
km = Kilometer(96.5606)
print(km.to_si())
print(mile < km)
