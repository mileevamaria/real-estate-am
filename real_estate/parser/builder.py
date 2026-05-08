from urllib.parse import urlencode, urlparse, parse_qs

from werkzeug.datastructures import MultiDict

from real_estate.parser import QUERY_SCHEMA, ParserConfig


class ParserQueryBuilder:
    def __init__(self):
        self._query = QUERY_SCHEMA.copy()

    def from_request_args(self, args):
        for key, value in dict(args.lists()).items():
            self._query[key] = ','.join(value)
        return self

    def build(self, base=False):
        url = ParserConfig.BASE_URL
        query_string = urlencode(self._query)
        if base:
            url = f'{url}&{ParserConfig.BASE_QUERY}'
        elif query_string:
            url = f'{url}&{query_string}'
        return url
    
    def base_request_args(self):
        url = self.build(base=True)
        params = parse_qs(
            urlparse(url).query,
            keep_blank_values=True,
        )
        return MultiDict(
            (key, item)
            for key, values in params.items()
            for value in values
            for item in value.split(',')
        )
