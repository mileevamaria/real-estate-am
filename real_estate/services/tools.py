import re

from real_estate.db.models import CurrencyEnum


def parse_price(raw_price: str) -> tuple[float, CurrencyEnum]:
    raw_price = raw_price.strip()
    currency = CurrencyEnum.AMD
    if '$' in raw_price:
        currency = CurrencyEnum.USD
    elif '€' in raw_price:
        currency = CurrencyEnum.EUR
    value = (
        raw_price
        .replace('$', '')
        .replace('€', '')
        .replace('֏', '')
        .replace(',', '')
        .strip()
    )
    return float(value), currency


def parse_attr(attr: str) -> dict[str, int]:
    '''
    2 ком., 52 кв.м., 6/18 этаж
    '''

    parts = attr.split(',')
    rooms = int(parts[0].split()[0])
    square = int(
        re.search(r'\d+', parts[1]).group()
    )
    floor_match = re.search(
        r'(\d+)/(\d+)',
        parts[2],
    )
    floor = int(floor_match.group(1))
    max_floor = int(floor_match.group(2))

    return {
        'rooms': rooms,
        'square': square,
        'floor': floor,
        'max_floor': max_floor,
    }
