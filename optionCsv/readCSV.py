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
    filepath = r"C:\Users\mt\Desktop\统计汇总\总量的文件列表.csv"

    newlist = []
    orglist = []

    with open(filepath, 'r') as r:
        reader = csv.reader(r)

        for item in reader:
            filenametemp = item[2]
            ret = filenametemp.find('(0')
            if ret > 0:
                realfilename = filenametemp[:ret]
            else:
                realfilename = item[2]

            if realfilename in newlist:
                # pass
                print(realfilename, "-- 重复")
            else:
                newlist.append(realfilename)

    filepath1 = r"C:\Users\mt\Desktop\统计汇总\编辑1.TXT.txt"
    with open(filepath1, 'r') as r2:
        oneline = r2.readline()

        while oneline:
            orgfile = oneline.replace('\n', '')
            if orgfile not in orglist:
                orglist.append(orgfile)
            oneline = r2.readline()

    print("org:", len(orglist))
    print("new:", len(newlist))
    # with open(filepath + '.txt', 'w') as w2:
    #     for actfile in newlist:
    #         if actfile not in orglist:
    #             w2.write(actfile + '\n')

    # with open(r'C:\Users\mt\Desktop\统计汇总\实际的重复文件名.txt', 'w') as www:
    #     for myf in newlist:
    #         www.write(myf + '\n')

    # for ifile in orglist:
    #     if ifile not in newlist:
    #         print(ifile)