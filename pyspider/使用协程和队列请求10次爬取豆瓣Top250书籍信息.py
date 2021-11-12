# -*- coding : utf-8 -*-

from gevent import monkey
monkey.patch_all()

import requests
from gevent import queue
from bs4 import BeautifulSoup
import csv
import gevent
import time


def get_request_header():
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) '
                      'Chrome/84.0.4147.105 Safari/537.36'
    }

    return headers


def get_data(page_num: int):
    data = {
        'start': page_num
    }
    return data


def get_book_info(wk_q: gevent._gevent_cqueue.Queue, sp_num):
    while not wk_q.empty():
        global book_list
        page_num = wk_q.get_nowait()
        print('爬虫{pnum}开始请求第{num}页的书籍信息...'.format(num=page_num, pnum=sp_num))
        book_url = 'https://book.douban.com/top250'
        headers = get_request_header()
        post_data = get_data(page_num)
        response = requests.post(book_url, headers=headers, data=post_data)

        if response.status_code == 200:
            bs_book = BeautifulSoup(response.text, 'html.parser')
            bs_book_div = bs_book.find('div', class_='indent')
            books_tb = bs_book_div.find_all('table')
            for book in books_tb:
                # print(book)
                bk_name = book.find('div', class_='pl2').a.text
                bk_name = bk_name.strip().replace('\n', '').replace(' ', '')
                author = book.find('p', class_='pl').text.split('/')[0].strip()
                rat_num = book.find('span', class_="rating_nums").text
                book_list.append([bk_name, author, rat_num])


def write_to_csv(line_list: list):
    with open('book_info.csv', 'w', newline='', encoding='utf-8-sig') as f:
        csv_writer = csv.writer(f, dialect='excel')
        csv_writer.writerow(['书名', '作者', '评分'])
        csv_writer.writerows(line_list)
    print('已经存储{0}条数据到csv文件'.format(len(line_list)))


if __name__ == "__main__":
    start_time = time.time()
    # 创建队列
    work_queue = queue.Queue()
    # 向队列中添加任务
    for num in range(0, 226, 25):
        work_queue.put_nowait(num)

    book_list = []

    # 创建两个爬虫执行请求任务
    task_list = []
    for i in range(2):
        task = gevent.spawn(get_book_info, work_queue, i)
        task_list.append(task)

    gevent.joinall(task_list)  # 启动协程任务

    end_time = time.time()
    print('爬取数据用时：', end_time - start_time)

    print('开始存储数据...')
    write_to_csv(book_list)

    print('处理完毕...')
