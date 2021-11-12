# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import openpyxl


def get_request_param():
    param = {
        'channel': 'notification:user:233734707',
        'auth': '233734707_1614069413:6f273a089c8f44db4020dd1b7c8ddfdc3b4da35a'
    }

    return param


def get_request_header():
    headers = {
        'Origin': 'https://movie.douban.com',
        'Referer': 'https://movie.douban.com/chart',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    return headers


if __name__ == '__main__':
    headers = get_request_header()
    url_info = "https://movie.douban.com/chart"

    print('开始抓取数据...')

    param = get_request_param()
    response = requests.get(url_info, params=param, headers=headers)
    bs_move = BeautifulSoup(response.text, 'html.parser')
    bs_div = bs_move.find("div", class_="indent")
    bs_div2 = bs_div.find_all('div', class_="pl2")

    print('开始整理数据...')
    mv_info_list = []
    for item in bs_div2:
        item_tag_a = item.find('a')
        mv_name = item_tag_a.text.replace('\n', '').split('/')[0].strip()
        mv_url = item_tag_a['href']
        mv_info = item.find('p', class_="pl").text
        mv_pifen = item.find('span', class_="rating_nums").text

        mv_info_list.append([mv_name, mv_url, mv_info, mv_pifen])

    if len(mv_info_list) > 0:
        print('开始存储数据...')
        mv_wb = openpyxl.Workbook()
        sheet = mv_wb.active
        sheet.title = '电影排行榜信息'
        sheet.append(['电影名字', '观看链接', '简介', '评分'])

        for item in mv_info_list:
            sheet.append(item)

        mv_wb.save("豆瓣电影排行信息.xlsx")
        mv_wb.close()
        print('存储数据完毕...')
    else:
        print('数据爬取失败')



