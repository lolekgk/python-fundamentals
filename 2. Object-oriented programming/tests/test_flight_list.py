from datetime import datetime, timedelta

import pytest
from flight_list import Airplane


@pytest.fixture
def landing_time():
    return datetime(2022, 8, 20, 14, 30)


@pytest.fixture
def start_time():
    return datetime(2022, 8, 20, 10, 30)


@pytest.fixture
def fake_landing_time():
    return datetime.now() + timedelta(hours=1)


@pytest.fixture
def fake_starting_time():
    return datetime.now() - timedelta(hours=1)


@pytest.fixture
def airplane(start_time, landing_time):
    return Airplane(815, 'Berlin', 'Warsaw', start_time, landing_time)


class TestAirplane:
    def test_status_without_start_time(self, landing_time):
        airplane = Airplane(815, 'Berlin', 'Warsaw', landing_time=landing_time)
        assert airplane.status == 'on the ground'

    def test_status_without_landing_time(self, start_time):
        airplane = Airplane(815, 'Berlin', 'Warsaw', start_time)
        assert airplane.status == 'on the ground'

    def test_status_when_airplane_is_flying(
        self, fake_starting_time, fake_landing_time
    ):
        airplane = Airplane(
            113, 'Madrid', 'Wroclaw', fake_starting_time, fake_landing_time
        )
        assert airplane.status == 'in the air'

    def test_status_after_landing(self, airplane):
        assert airplane.status == 'on the ground'

    def test_no_permission_for_creating_objects_with_the_same_attributes(self):
        airplane1 = Airplane(815, 'Berlin', 'Warsaw', start_time, landing_time)
        with pytest.raises(ValueError):
            airplane2 = Airplane(
                815, 'Berlin', 'Warsaw', start_time, landing_time
            )

    def test_flight_time_with_provided_dates(self, airplane):
        assert airplane.flight_time() == timedelta(seconds=14400)

    def test_flight_time_without_provided_dates(self):
        airplane = Airplane(815, 'Berlin', 'Warsaw')
        with pytest.raises(ValueError):
            airplane.flight_time()

    def test_list_all_flights(self):
        airplane1 = Airplane(815, 'Berlin', 'Warsaw', start_time, landing_time)
        airplane2 = Airplane(
            211, 'London', 'New York', start_time, landing_time
        )
        assert len(airplane1.list_all_flights()) == 2
        assert len(airplane1.list_all_flights()) == len(
            airplane2.list_all_flights()
        )
        for flight in airplane1.list_all_flights():
            assert isinstance(flight, Airplane)
