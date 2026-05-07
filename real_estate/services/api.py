import cloudscraper


def parse(url: str) -> None | dict:
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    if not response.ok:
        error = (
            f'Failed, status code {response.status_code}, '
            f'response: {response.text[:500]}'
        )
        raise ConnectionError(error)
    else:
        return response.json()
