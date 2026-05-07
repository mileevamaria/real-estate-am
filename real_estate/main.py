from real_estate import GlobalConfig
from real_estate.db import DatabaseConfig
from real_estate.services import collect_apartments, scheduler


def main():
    GlobalConfig.setup_logging()
    DatabaseConfig.init_db()
    collect_apartments()
    scheduler.start()


if __name__ == "__main__":
    main()