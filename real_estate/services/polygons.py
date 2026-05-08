from shapely import Point
from shapely.geometry import shape

from real_estate.db import DatabaseConfig
from real_estate.db.models import Apartment, Polygon


def is_polygon_contais_apartment(
    polygon: Polygon, 
    apartment: Apartment,
) -> bool:
    
    geojson = polygon.geojson
    geometry = shape(geojson['features'][0]['geometry'])
    point = Point(apartment.lon, apartment.lat)
    return geometry.intersects(point)


def save_polygon(data: dict) -> None:
    with DatabaseConfig.session() as session:
        polygon_name = data['name']
        polygon = (
            session.query(Polygon)
            .filter_by(name=polygon_name)
            .first()
        )
        if polygon:
            polygon.geojson = data
        else:
            polygon = Polygon(**data)
            session.add(polygon)
        session.commit()


def get_polygons() -> list:
    polygons = []
    with DatabaseConfig.session() as session:
        db_data = session.query(
            Polygon
        ).all()
        polygons = [data.geojson for data in db_data]
    return polygons
