from __future__ import annotations

# type['Person'] czy ten import? -> powinno działać od 3.10 bez powyzszego importu, lecz nie działa


class Person:
    def __init__(
        self, first_name: str, surname: str, second_name=None, address=None
    ):
        self.first_name = first_name
        self.surname = surname
        self.second_name = second_name
        self._acquaintances = []
        self._address = address

    def __repr__(self):
        return (
            f"Person(first_name='{self.first_name}', "
            f"second_name='{self.second_name}', "
            f"surname='{self.surname}', "
            f'address="{self._address})"'
        )

    def __str__(self):
        return (
            f"First name: {self.first_name}, "
            f"Second name: {self.second_name}, "
            f"Surname: {self.surname}, "
            f'Address: {self._address.street} {self._address.zipcode} '
            f'{self._address.city} {self._address.state} '
        )

    def _validate_user_input(self, user_input, var_name):
        if not isinstance(user_input, str):
            raise TypeError(
                f'The value of "{var_name}" should be of type str.'
            )
        elif len(user_input) < 2:
            raise ValueError(
                f'The length of "{var_name}" should be 2 at least.'
            )

    @property
    def email(self):
        return f'{self.first_name}.{self.surname}@gmail.com'.lower()

    @property
    def acquaintances(self):
        return self._acquaintances

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        Person._validate_user_input(self, first_name, 'first_name')
        self._first_name = first_name

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, second_name: str):
        if second_name:
            Person._validate_user_input(self, second_name, 'second_name')
        self._second_name = second_name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        Person._validate_user_input(self, surname, 'surname')
        self._surname = surname

    def add_acquaintance(self, acquaintance: type[Person]) -> None:
        if not isinstance(acquaintance, Person):
            raise TypeError('Acquaintance should be of type Person.')
        elif acquaintance not in self._acquaintances:
            self._acquaintances.append(acquaintance)

    def delete_acquaintance(self, acquaintance: type[Person]) -> None:
        if acquaintance in self._acquaintances:
            self._acquaintances.remove(acquaintance)


class Address:
    def __init__(
        self, street: str, city: str, state: str, zipcode: int
    ) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __repr__(self):
        return (
            f"Address(street='{self.street}', "
            f"city='{self.city}', "
            f"state='{self.state}', "
            f"zipcode='{self.zipcode})' "
        )

    def __str__(self):
        return (
            f"Street: {self.street}, "
            f"Zipcode: {self.zipcode}), "
            f"City: {self.city}, "
            f"State: {self.state} "
        )

    def _validate_user_input(self, user_input, var_name):
        if not isinstance(user_input, str):
            raise TypeError(
                f'The value of "{var_name}" should be of type str.'
            )

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        Address._validate_user_input(self, value, 'street')
        self._street = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        Address._validate_user_input(self, value, 'city')
        self._city = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        Address._validate_user_input(self, value, 'state')
        self._state = value

    @property
    def zipcode(self):
        return self._zipcode

    @zipcode.setter
    def zipcode(self, value):
        if not isinstance(value, int):
            raise TypeError('Zipcode should be of the type int.')
        self._zipcode = value
