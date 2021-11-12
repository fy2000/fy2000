# -*- coding:utf-8 -*-
import os
import sys
import csv


def get_carrier_id(strcarrier: str):
    if strcarrier == "中国移动":
        return 1
    if strcarrier == "中国联通":
        return 2
    if strcarrier == "中国电信":
        return 3


if __name__ == '__main__':
    filepath = r"C:\Users\mt\Desktop\统计汇总\all_file.csv"

    newlist = []
    orglist = []

    with open(filepath, 'r') as r:
        reader = csv.reader(r)

        for item in reader:
            realcarrier = 0
            filenametemp = item[2]
            # print(filenametemp.find("移动"))
            if filenametemp.find("移动") >= 0:
                realcarrier = 1
            elif filenametemp.find('联通') >= 0:
                realcarrier = 2
            elif filenametemp.find('电信') >= 0:
                realcarrier = 3
            else:
                continue

            if get_carrier_id(item[13]) != realcarrier:
                print([item[2], get_carrier_id(item[13])])
