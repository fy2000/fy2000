# -*- coding:utf-8 -*-

import requests

if __name__ == '__main__':
    headers = {
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/portal/search.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url_info = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"

    for i in range(3):
        param = {
            'ct': '24',
            'qqmusic_ver': '1298',
            'remoteplace': 'txt.yqq.lyric',
            'searchid': '92291369692947738',
            'aggr': '0',
            'catZhida': '1',
            'lossless': '0',
            'sem': '1',
            't': '7',
            'p': i + 1,
            'n': '5',
            'w': '五月天',
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

        response = requests.get(url_info, params=param, headers=headers)
        js_music = response.json()
        # print(js_music)
        js_list = js_music['data']
        lyric_list = js_list['lyric']['list']

        for item in lyric_list:
            print(item['content'])


