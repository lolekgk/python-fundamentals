import uuid
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
    airplane = Airplane(815, 'Berlin', 'Warsaw', start_time, landing_time)
    yield airplane
    del Airplane._flights[airplane.flight_id], airplane


@pytest.fixture
def airplane_without_start_time(landing_time):
    airplane = Airplane(815, 'Berlin', 'Warsaw', landing_time=landing_time)
    yield airplane
    del Airplane._flights[airplane.flight_id], airplane


@pytest.fixture
def airplane_without_landing_time(start_time):
    airplane = Airplane(815, 'Berlin', 'Warsaw', start_time)
    yield airplane
    del Airplane._flights[airplane.flight_id], airplane


@pytest.fixture
def flying_airplane(fake_starting_time, fake_landing_time):
    airplane = Airplane(
        113, 'Madrid', 'Wroclaw', fake_starting_time, fake_landing_time
    )
    yield airplane
    del Airplane._flights[airplane.flight_id], airplane


@pytest.fixture
def airplane_without_dates():
    airplane = Airplane(113, 'Madrid', 'Wroclaw')
    yield airplane
    del Airplane._flights[airplane.flight_id], airplane


@pytest.fixture
def flight_id():
    return uuid.uuid4()


class TestAirplane:
    def test_status_without_start_time(self, airplane_without_start_time):
        assert airplane_without_start_time.status == 'on the ground'

    def test_status_without_landing_time(self, airplane_without_landing_time):
        assert airplane_without_landing_time.status == 'on the ground'

    def test_status_when_airplane_is_flying(self, flying_airplane):
        assert flying_airplane.status == 'in the air'

    def test_status_after_landing(self, airplane):
        assert airplane.status == 'on the ground'

    def test_flight_time_with_provided_dates(self, airplane):
        assert airplane.flight_time() == timedelta(seconds=14400)

    def test_flight_time_without_provided_dates(self, airplane_without_dates):
        with pytest.raises(ValueError):
            airplane_without_dates.flight_time()

    def test_no_permission_for_creating_objects_with_the_same_attributes(
        self, flight_id
    ):
        airplane = Airplane(
            810, 'Berlin', 'Warsaw', start_time, landing_time, flight_id
        )
        with pytest.raises(ValueError):
            airplane = Airplane(
                810, 'Berlin', 'Warsaw', start_time, landing_time, flight_id
            )
        del Airplane._flights[airplane.flight_id], airplane

    def test_list_all_flights(self, airplane, flying_airplane):
        assert len(airplane.list_all_flights()) == 2
        assert len(airplane.list_all_flights()) == len(
            flying_airplane.list_all_flights()
        )
        for flight in airplane.list_all_flights().values():
            assert isinstance(flight, Airplane)
