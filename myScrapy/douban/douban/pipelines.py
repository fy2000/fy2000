# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class DoubanPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['书名', '评论id', '短评'])

    def process_item(self, item, spider):
        line_data = [item['name'], item['id'], item['comment']]
        self.ws.append(line_data)
        return item

    def close_spider(self, spider):
        self.wb.save('book_douban_comment.xlsx')
        self.wb.close()
