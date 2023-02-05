import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_scraper.scraper.spiders.sreality_spider import SRealitySpider
from scrapy_scraper.models import Base
from scrapy_scraper.models import Flat
from scrapy_scraper import engine, Session

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

    # Delete old records.
    with Session.begin() as session:
        session.query(Flat).delete()
        session.commit()

    process = CrawlerProcess()
    process.crawl(SRealitySpider)
    process.start()
