from __future__ import annotations


class Person:
    def __init__(
        self,
        first_name: str,
        surname: str,
        second_name: str = None,
        address: type[Address] = None,
    ):
        self.first_name = first_name
        self.surname = surname
        self.second_name = second_name
        self._acquaintances = []
        self._address = address

    def __repr__(self) -> str:
        return (
            f"Person(first_name='{self.first_name}', "
            f"second_name='{self.second_name}', "
            f"surname='{self.surname}', "
            f'address="{repr(self.address)}"'
        )

    def __str__(self) -> str:
        return (
            f"First name: {self.first_name}, "
            f"Second name: {self.second_name}, "
            f"Surname: {self.surname}, "
            f"Email: {self.email}, "
            f'Address: {self.address.street} {self.address.zipcode} '
            f'{self.address.city} {self.address.state}'
        )

    def __eq__(self, other) -> bool:
        return all(
            [
                self.first_name == other.first_name,
                self.surname == other.surname,
                self.second_name == other.second_name,
            ]
        )

    def _validate_user_input(self, user_input, var_name):
        if not isinstance(user_input, str):
            raise TypeError(
                f'The value of "{var_name}" should be of type str.'
            )
        if len(user_input) < 2:
            raise ValueError(
                f'The length of "{var_name}" should be 2 at least.'
            )

    @property
    def email(self) -> str:
        return f'{self.first_name}.{self.surname}@gmail.com'.lower()

    @property
    def acquaintances(self) -> list:
        return self._acquaintances

    @property
    def address(self) -> type[Address]:
        return self._address

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        Person._validate_user_input(self, first_name, 'first_name')
        self._first_name = first_name

    @property
    def second_name(self) -> str:
        return self._second_name

    @second_name.setter
    def second_name(self, second_name: str):
        if second_name:
            Person._validate_user_input(self, second_name, 'second_name')
        self._second_name = second_name

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        Person._validate_user_input(self, surname, 'surname')
        self._surname = surname

    def add_acquaintance(self, acquaintance: type[Person]):
        if not isinstance(acquaintance, Person):
            raise TypeError('Acquaintance should be of type Person.')
        elif acquaintance not in self._acquaintances:
            self._acquaintances.append(acquaintance)

    def delete_acquaintance(self, acquaintance: type[Person]):
        if acquaintance in self._acquaintances:
            self._acquaintances.remove(acquaintance)


class Address:
    def __init__(self, street: str, city: str, state: str, zipcode: int):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __repr__(self) -> str:
        return (
            f"Address(street='{self.street}', "
            f"city='{self.city}', "
            f"state='{self.state}', "
            f"zipcode='{self.zipcode}')"
        )

    def __str__(self) -> str:
        return (
            f"Street: {self.street}, "
            f"Zipcode: {self.zipcode}, "
            f"City: {self.city}, "
            f"State: {self.state}"
        )

    def __eq__(self, other) -> bool:
        return all(
            [
                self.street == other.street,
                self.city == other.city,
                self.zipcode == other.zipcode,
                self.state == other.state,
            ]
        )

    def _validate_user_input(self, user_input, var_name):
        if not isinstance(user_input, str):
            raise TypeError(
                f'The value of "{var_name}" should be of type str.'
            )

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, value: str):
        Address._validate_user_input(self, value, 'street')
        self._street = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str):
        Address._validate_user_input(self, value, 'city')
        self._city = value

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str):
        Address._validate_user_input(self, value, 'state')
        self._state = value

    @property
    def zipcode(self) -> int:
        return self._zipcode

    @zipcode.setter
    def zipcode(self, value: int):
        if not isinstance(value, int):
            raise TypeError('Zipcode should be of the type int.')
        self._zipcode = value
