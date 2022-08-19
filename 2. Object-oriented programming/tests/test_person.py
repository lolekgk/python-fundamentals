import pytest
from person import Address, Person


@pytest.fixture
def address():
    return Address('Kwiatowa 10/2', 'Warszawa', 'Mazowieckie', 30222)


@pytest.fixture
def person():
    return Person('Joshua', 'Kowalski', 'Brad')


@pytest.fixture
def test_friend1():
    return Person('Mark', 'Frame')


@pytest.fixture
def test_friend2():
    return Person('Rob', 'Holding')


class TestPerson:
    def test_user_creation_with_address_and_second_name(self, address):
        person = Person('Joshua', 'Kowalski', 'Brad', address)
        assert person.first_name == 'Joshua'
        assert person.surname == 'Kowalski'
        assert person.second_name == 'Brad'
        assert person.email == 'joshua.kowalski@gmail.com'
        assert person.address.street == 'Kwiatowa 10/2'
        assert person.address.city == 'Warszawa'
        assert person.address.state == 'Mazowieckie'
        assert person.address.zipcode == 30222
        assert person.acquaintances == []

    def test_the_same_person_objects_eq(self, person):
        person2 = Person('Joshua', 'Kowalski', 'Brad')
        assert person == person2

    def test_different_person_objects_eq(self, person):
        person1 = Person('Bart', 'Kowalski', 'Brad')
        assert person1 != person

    def test_user_creation_only_two_attributes_are_required(
        self, test_friend1
    ):
        assert test_friend1.first_name == 'Mark'
        assert test_friend1.surname == 'Frame'
        assert test_friend1.email == 'mark.frame@gmail.com'
        assert test_friend1.address is None
        assert test_friend1.second_name is None
        assert test_friend1.acquaintances == []

    def test_add_acquaintance_add_different_friend_objects(
        self, person, test_friend1, test_friend2
    ):
        person.add_acquaintance(test_friend1)
        person.add_acquaintance(test_friend2)
        assert person.acquaintances[0] == test_friend1
        assert person.acquaintances[1] == test_friend2
        assert len(person.acquaintances) == 2

    def test_add_acquaintance__add_the_same_objects(
        self, person, test_friend1, test_friend2
    ):
        person.add_acquaintance(test_friend1)
        person.add_acquaintance(test_friend1)
        person.add_acquaintance(test_friend2)
        person.add_acquaintance(test_friend2)
        assert person.acquaintances[0] == test_friend1
        assert person.acquaintances[1] == test_friend2
        assert len(person.acquaintances) == 2

    def test_delete_acquaintance_different_friend_objects(
        self, person, test_friend1, test_friend2
    ):
        person.add_acquaintance(test_friend1)
        person.add_acquaintance(test_friend2)
        person.delete_acquaintance(test_friend2)
        assert len(person.acquaintances) == 1

    def test_delete_acquaintance_delete_same_object_twice(
        self, person, test_friend1, test_friend2
    ):
        person.add_acquaintance(test_friend1)
        person.add_acquaintance(test_friend2)
        person.delete_acquaintance(test_friend2)
        person.delete_acquaintance(test_friend2)
        assert len(person.acquaintances) == 1

    def test_user_email_change_after_name_and_surname_change(self, person):
        person.first_name = 'Gabriel'
        person.surname = 'Jesus'
        assert person.email == 'gabriel.jesus@gmail.com'

    def test_add_acquaintance_validation(self, person):
        with pytest.raises(TypeError):
            person.add_acquaintance('friend')

    def test_first_name_init_validation_not_str(self):
        with pytest.raises(TypeError):
            Person(1, 'Kowalski', 'Brad')

    def test_second_name_init_validation_not_str(self):
        with pytest.raises(TypeError):
            Person('Jan', 'Kowalski', 1)

    def test_surname_init_validation_not_str(self):
        with pytest.raises(TypeError):
            Person('Jan', 1, 'Kowal')

    def test_first_name_init_validation_len(self):
        with pytest.raises(ValueError):
            Person('J', 'Kowalski', 'Brad')

    def test_second_name_init_validation_len(self):
        with pytest.raises(ValueError):
            Person('Jan', 'Kowalski', 'Z')

    def test_surname_init_validation_len(self):
        with pytest.raises(ValueError):
            Person('Jan', 'B', 'Brad')

    def test_first_name_set_attribute_validation_not_str(self, person):
        with pytest.raises(TypeError):
            person.first_name = 10

    def test_second_name_set_attribute_validation_not_str(self, person):
        with pytest.raises(TypeError):
            person.second_name = 10

    def test_surname_set_attribute_validation_not_str(self, person):
        with pytest.raises(TypeError):
            person.surname = True

    def test_first_name_set_attribute_validation_len(self, person):
        with pytest.raises(ValueError):
            person.first_name = 'T'

    def test_second_name_set_attribute_validation_len(self, person):
        with pytest.raises(ValueError):
            person.second_name = 'T'

    def test_surname_set_attribute_validation_len(self, person):
        with pytest.raises(ValueError):
            person.surname = 'T'


class TestAddress:
    def test_address_creation(self, address):
        assert address.street == 'Kwiatowa 10/2'
        assert address.city == 'Warszawa'
        assert address.state == 'Mazowieckie'
        assert address.zipcode == 30222

    def test_the_same_address_objects_eq(self, address):
        address2 = Address('Kwiatowa 10/2', 'Warszawa', 'Mazowieckie', 30222)
        assert address == address2

    def test_different_address_objects_eq(self, address):
        address2 = Address('Kwiatowa 12/2', 'Warszawa', 'Mazowieckie', 30222)
        assert address != address2

    def test_street_init_validation_not_str(self):
        with pytest.raises(TypeError):
            Address(1, 'Warszawa', 'Mazowieckie', 30222)

    def test_city_init_validation_not_str(self):
        with pytest.raises(TypeError):
            Address('Angielska', 1, 'Mazowieckie', 30222)

    def test_state_init_validation_not_str(self):
        with pytest.raises(TypeError):
            Address('Kwiatowa', 'Warszawa', 1, 30222)

    def test_zipcode_init_validation_not_int(self):
        with pytest.raises(TypeError):
            Address('Kwiatowa', 'Warszawa', 'test', '50222')

    def test_street_set_attribute_validation_not_str(self, address):
        with pytest.raises(TypeError):
            address.street = 10

    def test_city_set_attribute_validation_not_str(self, address):
        with pytest.raises(TypeError):
            address.city = False

    def test_state_set_attribute_validation_not_str(self, address):
        with pytest.raises(TypeError):
            address.state = [1, 2]

    def test_zipcode_set_attribute_validation_not_int(self, address):
        with pytest.raises(TypeError):
            address.zipcode = 'code'
