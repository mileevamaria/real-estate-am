from datetime import datetime
from enum import Enum
from urllib.parse import urljoin

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from real_estate.db import Base
from real_estate.parser import ParserConfig


class CurrencyEnum(str, Enum):
    AMD = 'AMD'
    USD = 'USD'
    EUR = 'EUR'


class Apartment(Base):
    __tablename__ = "apartments"

    id: Mapped[int] = mapped_column(primary_key=True)
    listing_id: Mapped[str] = mapped_column(
        String, unique=True, index=True,
    )
    price: Mapped[float] = mapped_column(Float)
    currency: Mapped[CurrencyEnum] = mapped_column(SqlEnum(CurrencyEnum))
    lon: Mapped[float] = mapped_column(Float)
    lat: Mapped[float] = mapped_column(Float)
    address: Mapped[str | None] = mapped_column(String)
    square: Mapped[int] = mapped_column(Integer)
    rooms: Mapped[int] = mapped_column(Integer)
    floor: Mapped[int] = mapped_column(Integer)
    max_floor: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )

    @property
    def apartment_url(self):
        return urljoin(ParserConfig.BASE_URL_APARTMENT, self.listing_id)

    @property
    def price_per_sqm(self):
        return round(self.price / self.square, 2)
    