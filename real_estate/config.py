import os

import rollbar
import rollbar.contrib.flask
from dotenv import load_dotenv
from flask import got_request_exception

load_dotenv()


class Config:
    YANDEX_MAPS_API_KEY = os.getenv('YANDEX_MAPS_API_KEY')
    ROLLBAR_ACCESS_TOKEN = os.getenv('ROLLBAR_ACCESS_TOKEN')
    ROLLBAR_ENVIRONMENT = os.getenv('ROLLBAR_ENVIRONMENT')


def init_rollbar(app):
    if not Config.ROLLBAR_ENVIRONMENT:
        return
    
    # Initialize Rollbar
    rollbar.init(
        access_token=Config.ROLLBAR_ACCESS_TOKEN,
        environment=Config.ROLLBAR_ENVIRONMENT,
        # Root directory for cleaner stack traces
        root=os.path.dirname(os.path.realpath(__file__)),
        # Flask handles logging setup
        allow_logging_basic_config=False,
    )

    # Connect Flask signals to Rollbar
    got_request_exception.connect(
        rollbar.contrib.flask.report_exception,
        app
    )
