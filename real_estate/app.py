from flask import Flask, render_template, request

from .config import Config, init_rollbar
from .filters import Currency, Location, Ownership, Rooms
from .services import ListAmQueryBuilder, parse

app = Flask(__name__)

init_rollbar(app)


@app.route('/')
def index():
    builder = ListAmQueryBuilder()
    builder.from_request_args(request.args)
    generated_url = builder.build()
    data = parse(generated_url)
    map_api_key = Config.YANDEX_MAPS_API_KEY

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
