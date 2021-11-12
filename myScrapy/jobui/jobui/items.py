# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobJobuiItem(scrapy.Item):
    # 存放书名
    company = scrapy.Field()

    # 职位名称
    position = scrapy.Field()

    # 公司地点
    address = scrapy.Field()

    # 详情信息
    detail = scrapy.Field()
