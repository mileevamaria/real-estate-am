from enum import Enum


class ListAmQueryEnum(Enum):
    def __init__(self, value: int, label: str | None = None):
        self._value_ = value
        self.label = label

    @property
    def query_name(self):
        return self._query_name

    @query_name.setter
    def query_name(self, value):
        self._query_name = value


class Location(ListAmQueryEnum):
    KENTRON = 8, 'Кентрон'
    ARABKIR = 3, 'Арабкир'


Location.query_name = 'n'


class Ownership(ListAmQueryEnum):
    OWNER = 0, 'Собственник'
    AGENCY = 1, 'Агентство'


Ownership.query_name = 'cmtype'


class Currency(ListAmQueryEnum):
    AMD = 0, 'Драм'
    USD = 1, 'Доллар'


Currency.query_name = 'crc'


class Rooms(ListAmQueryEnum):
    ONE = 1, '1'
    TWO = 2, '2'
    THREE = 3, '3'
    FOUR = 4, '4'
    FIVE = 5, '5'


Rooms.query_name = '_a4'


class NewlyBuilt(ListAmQueryEnum):
    NO = 1, 'Нет'
    YES = 2, 'Да'


NewlyBuilt.query_name = '_a39'


class Elevator(ListAmQueryEnum):
    NO = 2, 'Нет'
    YES = 1, 'Да'


Elevator.query_name = '_a40'
