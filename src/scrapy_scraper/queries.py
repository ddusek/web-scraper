from sqlalchemy import select
from scrapy_scraper.models import Flat
from scrapy_scraper import Session


def retrieve_flats():
    with Session.begin() as session:
        statement = select(Flat).limit(500)
        flats = session.scalars(statement).all()
        return [flat.as_dict() for flat in flats]
