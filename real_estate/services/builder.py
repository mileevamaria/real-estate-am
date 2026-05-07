from urllib.parse import urlencode

from real_estate.filters import QUERY_SCHEMA


class ListAmQueryBuilder:
    BASE_URL = 'https://www.list.am/ru/aj-category-map?c=60&gl=8'
    QUERY_EXAMPLE = 'n=8,3&_a39=2&_a11_1=5&_a4=2'

    def __init__(self):
        self._query = QUERY_SCHEMA.copy()

    def from_request_args(self, args):
        for key, value in dict(args.lists()).items():
            self._query[key] = ','.join(value)
        return self

    def build(self):
        url = self.BASE_URL
        query_string = urlencode(self._query)
        if query_string:
            url = f'{url}&{query_string}'
        return url
