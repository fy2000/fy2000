# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookDangdangItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
