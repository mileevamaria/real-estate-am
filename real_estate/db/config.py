import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()


class Base(DeclarativeBase):
    pass


class DatabaseConfig:

    DATABASE_URL = os.getenv('DATABASE_URL')

    if not DATABASE_URL:
        raise ValueError('DATABASE_URL is not set')

    engine = create_engine(DATABASE_URL, echo=False)
    
    session = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )

    @classmethod
    def init_db(cls):
        Base.metadata.create_all(bind=cls.engine)
