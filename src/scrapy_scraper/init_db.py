import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_scraper.scrapy_scraper.spiders.sreality_spider import SRealitySpider

if __name__ == '__main__':
    process = CrawlerProcess(settings={
        'FEEDS': {
            'items.json': {'format': 'json'},
        }
    })
    process.crawl(SRealitySpider)
    process.start()
