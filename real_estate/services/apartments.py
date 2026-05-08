import logging

import cloudscraper

from real_estate.db import DatabaseConfig
from real_estate.db.models import Apartment
from real_estate.parser.builder import ParserQueryBuilder
from real_estate.services.tools import parse_attr, parse_price

logger = logging.getLogger(__name__)


def fetch_apartments(url: str) -> list[dict]:
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    if not response.ok:
        error = (
            f'fetch_apartments: failed, status code {response.status_code}, '
            f'response: {response.text[:500]}'
        )
        raise ConnectionError(error)
    else:
        result = response.json()
        if 'data' not in result:
            error = (
                f'fetch_apartments: unexpected json structure, '
                f'response: {response.text[:500]}'
            )
            raise ValueError(error)
    return result['data']


def collect_apartments() -> None:
    logger.info('start parsing apartments')
    url_builder = ParserQueryBuilder()
    url = url_builder.build(base=True)
    apartments = fetch_apartments(url)
    logger.info('fetched %s apartments', len(apartments))
    save_apartments(apartments)
    logger.info('apartments saved')


def parse_apartments(groups: list[dict]) -> list:
    apartments = []
    for group in groups:
        lat = float(group['lat'])
        lon = float(group['lng'])
        for item in group['data']:
            price, currency = parse_price(
                item['price']
            )
            attrs = parse_attr(item['attr'])
            apartment = {
                'listing_id': item['id'],
                'price': price,
                'currency': currency,
                'lat': lat,
                'lon': lon,
                **attrs,
            }
            apartments.append(apartment)
    return apartments


def save_apartments(apartments: list[dict]) -> None:
    normalized_appartments = parse_apartments(apartments)
    logger.info(f'normalized_appartments: {normalized_appartments[:10]}')
    with DatabaseConfig.session() as session:
        for item in normalized_appartments:
            exists = (
                session.query(Apartment)
                .filter_by(listing_id=item['listing_id'])
                .first()
            )
            if exists:
                continue
            apartment = Apartment(**item)
            session.add(apartment)
        session.commit()


