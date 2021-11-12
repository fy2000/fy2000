# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
from ..items import JobJobuiItem


class GetJobSpider(scrapy.Spider):
    name = 'job_jobui'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        bs = BeautifulSoup(response.text, 'html.parser')
        bs_div_tag = bs.find('div', class_='searchCont')
        bs_ul_tags = bs_div_tag.find_all('ul')
        for ul_tag in bs_ul_tags:
            bs_li_tags = ul_tag.find_all('li')
            for li_tag in bs_li_tags[:3]:
                company_id = li_tag.a['href']
                url = 'https://www.jobui.com{0}jobs/'.format(company_id)
                yield scrapy.Request(url, callback=self.parse_getjobinfo)

    def parse_getjobinfo(self, response):
        bs = BeautifulSoup(response.text, 'html.parser')
        company_name = bs.find('a', class_='company-banner-name').text

        positions = bs.find_all('div', class_='job-simple-content')

        for job in positions:
            job_name = job.find('a', class_='job-name').h3.text
            job_des = job.find('div', class_='job-desc').find_all('span')
            job_address = job_des[0].text
            job_details = job_des[1].text

            job_info = JobJobuiItem()
            job_info['company'] = company_name
            job_info['position'] = job_name
            job_info['address'] = job_address
            job_info['detail'] = job_details

            yield job_info

