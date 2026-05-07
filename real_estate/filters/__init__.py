from .enums import (
    Currency,
    Elevator,
    Location,
    NewlyBuilt,
    Ownership,
    Rooms,
)
from .ranges import (
    Floor,
    PricePerSqm,
    PriceTotal,
    SquareMeters,
)

QUERY_SCHEMA = {
    Location.query_name: '',
    Ownership.query_name: '',
    Currency.query_name: '',
    NewlyBuilt.query_name: '',
    Elevator.query_name: '',
    PriceTotal.from_query_name: '',
    PriceTotal.to_query_name: '',
    PricePerSqm.from_query_name: '',
    PricePerSqm.to_query_name: '',
    SquareMeters.from_query_name: '',
    SquareMeters.to_query_name: '',
    Floor.from_query_name: '',
    Floor.to_query_name: '',
    Rooms.query_name: '',
}

__all__ = (
    'Location',
    'Ownership',
    'Currency',
    'Rooms',
    'NewlyBuilt',
    'Elevator',
    'PricePerSqm',
    'PriceTotal',
    'Floor',
    'SquareMeters',
    'QUERY_SCHEMA',
)
