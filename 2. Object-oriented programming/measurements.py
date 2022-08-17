from abc import ABC, abstractmethod


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


class Celcius(Unit):
    quantity = 'temperature'
    unit_symbol = '°C'

    def to_si(self):
        return self.value + 273.15


class Fahrenheit(Unit):
    quantity = 'temperature'
    unit_symbol = '°F'

    def to_si(self):
        return (self.value + 459.67) * 5 / 9


class Centimeter(Unit):
    quantity = 'length'
    unit_symbol = 'cm'

    def to_si(self):
        return self.value * 0.01


class Inch(Unit):
    quantity = 'length'
    unit_symbol = '″'

    def to_si(self):
        return self.value * 0.0254


class Kilometer(Unit):
    quantity = 'length'
    unit_symbol = 'km'

    def to_si(self):
        return self.value * 1000


class Mile(Unit):
    quantity = 'length'
    unit_symbol = 'mi.'

    def to_si(self):
        return self.value * 1609.344


class Liter(Unit):
    quantity = 'volume'
    unit_symbol = 'L'

    def to_si(self):
        return self.value * 0.001


class Gallon(Unit):
    quantity = 'volume'
    unit_symbol = 'gal'

    def to_si(self):
        return self.value * 0.0037854118
