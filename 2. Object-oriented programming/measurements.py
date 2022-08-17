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
