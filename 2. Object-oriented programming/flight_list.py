import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Airplane:
    _flights = []

    flight_number: int
    destination: str
    origin: str
    start_time: datetime = field(default=None)
    landing_time: datetime = field(default=None)
    _flight_id: uuid = field(
        default_factory=uuid.uuid4, init=False, repr=False, compare=False
    )
    _status: str = field(default='on the ground', init=False, repr=False)

    def __post_init__(self):
        for flight in self._flights:
            if self == flight:
                raise ValueError(
                    'You cannot create flight with same attributes!'
                )
        self._flights.append(self)

    @property
    def flight_id(self):
        return self._flight_id

    @property
    def status(self) -> str:
        if self.start_time and self.landing_time is not None:
            if (
                self.start_time < datetime.now()
                and self.landing_time > datetime.now()
            ):
                self._status = 'in the air'
            else:
                self._status = 'on the ground'
        return self._status

    @property
    def _flight_number(self) -> int:
        return self._flight_number

    @property
    def _flight_id(self):
        return self._flight_id

    def flight_time(self) -> datetime:
        return self.landing_time - self.start_time

    @classmethod
    def list_all_flights(cls) -> list:
        return cls._flights
