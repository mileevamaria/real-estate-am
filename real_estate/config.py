import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class GlobalConfig:

    YANDEX_MAPS_API_KEY = os.getenv('YANDEX_MAPS_API_KEY')
    LOG_FORMAT = '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
    
    @classmethod
    def setup_logging(cls):
        formatter = logging.Formatter(cls.LOG_FORMAT)
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        log_dir = Path('logs')
        file_handler = RotatingFileHandler(
            log_dir / 'app.log',
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8',
        )
        file_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)
