import logging

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
)

from real_estate.config import GlobalConfig
from real_estate.parser import (
    Currency,
    Location,
    Ownership,
    Rooms,
)
from real_estate.parser.builder import ParserQueryBuilder
from real_estate.services import fetch_apartments
from real_estate.services.polygons import get_polygons, save_polygon

app = Flask(__name__)
app = GlobalConfig.set_secret_key(app)

GlobalConfig.setup_logging()
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def index():
    url_builder = ParserQueryBuilder()
    base = False
    selected = request.args
    if not request.args:
        base = True
        selected = url_builder.base_request_args()
    else:
        url_builder.from_request_args(selected)
        
    data_url = url_builder.build(base=base)
    data = fetch_apartments(data_url)
    map_api_key = GlobalConfig.YANDEX_MAPS_API_KEY

    logger.info(f'get_polygons(): {get_polygons()}')

    return render_template(
        'index.html',

        # select options
        locations=Location,
        ownerships=Ownership,
        currencies=Currency,
        rooms=Rooms,

        # current selected values
        selected=selected,

        # data
        flats=data,
        polygons=get_polygons(),
        map_api_key=map_api_key,
    )


@app.route('/poligon/save', methods=['POST'])
def save_poligon():
    geojson = request.json
    resp_data = {'message': 'Некорректный GeoJSON'}
    if not geojson:
        return jsonify(resp_data), 400
    
    try:
        feature = geojson['features'][0]
        polygon_name = (feature['properties']['name'].strip())
    except (KeyError, IndexError, TypeError):
        return jsonify(resp_data), 400
    
    data = {'name': polygon_name, 'geojson': geojson}
    save_polygon(data)
    resp_data = {'message': 'Полигон сохранен'}
    return jsonify(resp_data), 201
