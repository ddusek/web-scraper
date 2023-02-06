import os
from urllib.parse import urlencode
import scrapy
from scrapy_splash import SplashRequest
from scrapy_scraper.scraper.items import FlatItem

class SRealitySpider(scrapy.Spider):
    custom_settings = {'ITEM_PIPELINES': {'scraper.pipelines.PostgresPipeline': 300}}
    name = 'sreality-flats-sell'

    start_urls = [f'https://www.sreality.cz/hledani/prodej/byty?strana={i}' for i in range(2, 26)]
    start_urls.insert(0, 'https://www.sreality.cz/hledani/prodej/byty')

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.json',
                                args={
                                    'html': 1,
                                    'width': 1920,
                                })

    def parse(self, response):
        for flat in response.css('div.property'):
            title = flat.xpath('div/div/span/h2/a/span/text()').get()
            image = flat.xpath('preact/div/div/a/img').attrib['src']
            yield FlatItem(title, image)
