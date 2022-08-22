import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Airplane:
    flight_number: int
    destination: str
    origin: str
    start_time: datetime = field(default=None)
    landing_time: datetime = field(default=None)
    _flight_id: uuid = field(
        default_factory=uuid.uuid4, init=False, repr=False
    )
    _flights: list = field(default_factory=list, init=False, repr=False)
    _status: str = field(default='on the ground', init=False, repr=False)

    def __post_init__(self):
        self._flights.append(self)

    @property
    def flight_id(self):
        return self._flight_id

    @property
    def flights(self):
        return self._flights

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

    @status.setter
    def status(self, status: str):
        if not isinstance(status, str):
            raise TypeError(f'The value of "" should be of type str.')

    def flight_time(self):
        return self.landing_time - self.start_time

    @classmethod
    def list_all_flights(cls):
        return cls.flights
