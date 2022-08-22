import uuid
from datetime import datetime

import attr


@attr.s(slots=True, on_setattr=attr.setters)
class Airplane:
    _flights = []

    flight_number: int = attr.ib(
        validator=attr.validators.instance_of(int),
        on_setattr=attr.setters.validate,
    )
    destination: str = attr.ib(
        validator=attr.validators.instance_of(str),
        on_setattr=attr.setters.validate,
    )
    origin: str = attr.ib(
        validator=attr.validators.instance_of(str),
        on_setattr=attr.setters.validate,
    )
    _start_time: datetime = attr.ib(default=None)
    landing_time: datetime = attr.ib(default=None)
    _flight_id: uuid = attr.ib(default=None, init=False, repr=False)
    status: str = attr.ib(default='on the ground', init=False, repr=False)

    def __attrs_post_init__(self):
        if self.flight_number in [cls.flight_number for cls in self._flights]:
            raise ValueError('You cannot add the same flight!')
        self._flights.append(self)

    @property
    def flight_id(self):
        return self._flight_id

    @property
    def status(self):
        if (
            self.start_time < datetime.now()
            and self.landing_time > datetime.now()
        ):
            self._status = 'in the air'
        else:
            self._status = 'on the ground'
        return self._status

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        if start_time:
            if isinstance(start_time, datetime):
                self._start_time = start_time
        self._start_time = start_time

    def calculate_flight_time(self):
        return self.landing_time - self.start_time

    @classmethod
    def list_all_flights(cls):
        return cls._flights
