# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewsItem(scrapy.Item):
    url = scrapy.Field()
    raw_content = scrapy.Field()
    timestamp_crawl = scrapy.Field()
    doc_id = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
