import os
from urllib.parse import urlencode
import scrapy
from scrapy_splash import SplashRequest
from scrapy_scraper.database_connection import create_postgres_engine


def get_proxy_url(url: str) -> str:
    api_key = os.getenv('PROXY_API_KEY')
    payload = {'api_key': api_key, 'url': url, 'render_js': 'true'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class SRealitySpider(scrapy.Spider):
    engine = create_postgres_engine()

    name = 'flats-sell'
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']
    pagination = '?strana=2'

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=get_proxy_url(url),
                                callback=self.parse,
                                endpoint='render.json',
                                args={
                                    'html': 1,
                                    'width': 1920,
                                })

    def parse(self, response):
        for flat in response.css('div.property'):
            yield {
                'title': flat.xpath('div/div/span/h2/a/span/text()').get(),
                'image': flat.xpath('preact/div/div/a/img').attrib['src'],
            }

        next_page_node = response.css('li.paging-item')
        print(next_page_node)
