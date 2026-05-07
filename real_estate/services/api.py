import cloudscraper


def parse(url: str) -> None | dict:
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    if not response.ok:
        print(f'Failed, status code {response.status_code}')
        print(response.text[:500])
        return
    else:
        return response.json()
