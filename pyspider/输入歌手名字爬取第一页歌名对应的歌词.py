# -*- coding:utf-8 -*-

import requests


def get_request_param(singer: str):
    param = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '55398777443497423',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': '1',
        'n': '10',
        'w': singer,
        'g_tk_new_20200303': '1111655766',
        'g_tk': '1111655766',
        'loginUin': '574672787',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }

    return param


def get_request_header():
    headers = {
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/portal/search.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    return headers


if __name__ == '__main__':
    headers = get_request_header()
    url_info = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"

    print('**** 欢迎来到找歌词页面 ****')
    while True:
        print('=====================================')
        singer = input('请输入一个歌手的名字：')
        if singer is None:
            continue
        # 这里只爬取第一页的歌曲清单
        param = get_request_param(singer)
        response = requests.get(url_info, params=param, headers=headers)
        js_music = response.json()
        # print(js_music)
        js_list = js_music['data']
        music_list = js_list['song']['list']
        # print(music_list)
        for item in music_list:
            print(item['name'])

        isexit = input('是否退出(n/y): ')
        if isexit == 'y':
            break

    print('程序结束\n欢迎再来！')
