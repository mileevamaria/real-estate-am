import logging

from flask import Flask, render_template, request

from real_estate.config import GlobalConfig
from real_estate.parser import (
    Currency,
    Location,
    Ownership,
    Rooms,
)
from real_estate.parser.builder import ParserQueryBuilder
from real_estate.services import fetch_apartments

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def index():
    url_builder = ParserQueryBuilder()
    url_builder.from_request_args(request.args)
    data_url = url_builder.build()
    logger.info(f'list am url: {data_url}')
    data = fetch_apartments(data_url)
    map_api_key = GlobalConfig.YANDEX_MAPS_API_KEY

    return render_template(
        'index.html',

        # select options
        locations=Location,
        ownerships=Ownership,
        currencies=Currency,
        rooms=Rooms,

        # current selected values
        selected=request.args,

        # data
        flats=data,
        map_api_key=map_api_key,
    )
