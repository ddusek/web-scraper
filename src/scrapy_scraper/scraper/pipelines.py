# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from scrapy_scraper.models import Flat
from scrapy_scraper import Session

class PostgresPipeline:

    def __init__(self):
        self.session: Session
    
    # @classmethod
    # def from_crawler(cls, crawler):
    #     obj = cls(job_dir(crawler.settings))
    #     crawler.signals.connect(obj.spider_closed, signal=signals.spider_closed)
    #     crawler.signals.connect(obj.spider_opened, signal=signals.spider_opened)
    #     return obj

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        flat = Flat(title=adapter.get('title'), image=adapter.get('image'))
        self.session.add(flat)
        self.session.commit()
        return item

    def open_spider(self, spider):
        self.session = Session()
        
    def close_spider(self, spider):
        self.session.close()
