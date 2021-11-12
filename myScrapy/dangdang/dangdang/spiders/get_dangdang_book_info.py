# -*- coding: utf-8 -*-

import scrapy
from ..items import BookDangdangItem
from bs4 import BeautifulSoup


class BookDangdangSpider(scrapy.Spider):
    name = 'book_dangdang'
    allowed_domains = ['bang.dangdang.com']

    start_urls = []

    for i in range(1, 4):
        url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-{i}'
        start_urls.append(url)

    def parse(self, response):
        bs = BeautifulSoup(response.text, 'html.parser')
        bs_ul = bs.find('ul', class_='bang_list')
        bs_lis = bs_ul.find_all('li')

        for li_tag in bs_lis:
            book_name = li_tag.find('div', class_='name').a.text
            book_author = li_tag.find('div', class_='publisher_info').find('a').text
            book_price = li_tag.find('div', class_='price').p.find('span', class_='price_n').text

            book_info = BookDangdangItem()
            book_info['name'] = book_name.split('（')[0]
            book_info['author'] = book_author
            book_info['price'] = book_price

            yield book_info
