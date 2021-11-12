# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScommentDoubanItem(scrapy.Item):
    # 存放书名
    name = scrapy.Field()
    # 存放评论ID
    id = scrapy.Field()
    # 存放短评
    comment = scrapy.Field()
