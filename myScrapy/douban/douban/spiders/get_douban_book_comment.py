# -*- coding: utf-8 -*-

import scrapy
from ..items import ScommentDoubanItem
from bs4 import BeautifulSoup


class DoubanBookSComment(scrapy.Spider):
    name = 'scomment_douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        bs = BeautifulSoup(response.text, 'html.parser')

        bs_book_tbs = bs.find('div', class_='indent').find_all('table')

        for book_tag in bs_book_tbs[:3]:
            book_name = book_tag.find('div', class_='pl2').a.text
            bs_book_link = book_tag.find('div', class_='pl2').a['href']

            response = scrapy.Request(bs_book_link, callback=self.parse_scomment, cb_kwargs=dict(name=book_name))
            yield response

    def parse_scomment(self, response, name):
        bs = BeautifulSoup(response.text, 'html.parser')
        bs_div = bs.find('div', id='new_score')
        bs_book_lis = bs_div.ul.find_all('li', class_='comment-item')
        for book_li_tag in bs_book_lis:
            book_scomment = ScommentDoubanItem()
            book_scomment['name'] = name.replace('\n', '').replace(' ', '')
            book_scomment['id'] = book_li_tag.div.h3.find('span', class_='comment-info').a.text
            book_scomment['comment'] = book_li_tag.div.p.text.replace('\n', '')
            yield book_scomment
