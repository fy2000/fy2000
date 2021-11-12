# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class JobuiPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()  # 创建工作薄
        self.ws = self.wb.active  # 定位活动表
        self.ws.append(['公司', '职位', '地址', '招聘信息'])  # 用append函数往表格添加表头

    def process_item(self, item, spider):
        # 把公司名称、职位名称、工作地点和招聘要求都写成列表的形式，赋值给line
        line = [item['company'], item['position'], item['address'], item['detail']]
        # 用append函数把公司名称、职位名称、工作地点和招聘要求的数据都添加进表格
        self.ws.append(line)
        return item

    # close_spider是当爬虫结束运行时，这个方法就会执行
    def close_spider(self, spider):
        self.wb.save('JobInfo.xlsx')  # 保存文件
        self.wb.close()  # 关闭文件

