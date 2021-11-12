# -*- coding: utf-8 -*-

import datetime
from dbtools import get_info_from_db


def get_date_value(element):
    strtime = element["date"].split("/")
    time = datetime.datetime(int(strtime[0]), int(strtime[1]), 1, 0, 0, 0, 0)
    return time


def get_month_info():
    monthdict = {}
    sql = f"SELECT strdate FROM tb_total_sales_order_2020"
    monthinfo = get_info_from_db(sql)
    monthinfo = list(set(monthinfo))

    # 通过去重，获取日期维度的key值
    for item in monthinfo:
        vecdate = item[0].split("/")
        strdate = "%d/%d" % (int(vecdate[0]), int(vecdate[1]))
        monthdict[strdate] = {}

    # 根据key值获取相关的信息
    countlist = []  # 用来计算总和的
    for date in monthdict.keys():
        sql = f"SELECT strdate, iindex, strdocumentcode from tb_total_sales_order_2020 where strdate like '{date}%'"
        reqinfo = get_info_from_db(sql)
        monthdict[date]['count'] = len(reqinfo)
        countlist.append(monthdict[date]['count'])
    # 填充百分比
    sumvalue = sum(countlist)
    for item in monthdict.keys():
        ratio = round((monthdict[item]["count"] / sumvalue), 4)
        monthdict[item]["percent"] = ratio

    monthlist = []
    for date in monthdict.keys():
        monthlist.append({"date": date, "count": monthdict[date]["count"], "percent": monthdict[date]["percent"]})

    monthlist.sort(key=get_date_value)
    return monthlist


if __name__ == '__main__':
    sumnum = 0
    for item in get_month_info():
        print(item)
        sumnum += item["percent"]

    print("总和", sumnum)
