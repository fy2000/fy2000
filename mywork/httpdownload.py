# -*- coding: utf-8 -*-
import datetime
import csv
from modules.fileopt import list_file
from modules.csvopt import CsvOpt
import os


def decode_lte_http(file_all_name):
    datedic = {}
    starttime = datetime.datetime.now()
    endtime = datetime.datetime.now()
    curtime = datetime.datetime.now()

    lasdlsize = 0
    http_dl_size = 0.0
    totalsize = 0

    linelist = []

    httpnewloop = False

    with open(file_all_name, 'r') as f:
        strline = f.readline()
        while strline:
            if strline.startswith('DAY'):
                dayparts = strline.split('\t')
                datedic['year'] = int(dayparts[1])
                datedic['month'] = int(dayparts[2])
                datedic['day'] = int(dayparts[3])
            elif strline.startswith('HOUR'):
                hourparts = strline.split('\t')
                datedic['hour'] = int(hourparts[1])
            elif strline.startswith('MIN'):
                minparts = strline.split('\t')
                datedic['min'] = int(minparts[1])
            elif strline.startswith('SEC'):
                minparts = strline.split('\t')
                datedic['sec'] = int(minparts[1])
                datedic['msec'] = int(minparts[2])
                curtime = datetime.datetime(datedic['year'], datedic['month'], datedic['day'], datedic['hour'],
                                            datedic['min'], datedic['sec'], datedic['msec'] * 1000)
                # print(curtime)
            elif strline.startswith('APPLAYER'):
                # APPLAYER	HTTP		2011.023#2011.023###############15992.234#
                layerparts = strline.split('\t')
                if layerparts[1] != "HTTP":
                    pass
                else:
                    if httpnewloop:
                        speeds = layerparts[3].split('#')
                        totalsize = float(speeds[1]) if speeds[1] else 0  # Number of bytes transmitted for lte
                        http_dl_size = (totalsize - lasdlsize) * 8
                        lasdlsize = totalsize

            elif strline.startswith('APPEVENT'):
                # APPEVENT	HTTP	0x01019003-ms1-20211007082808-5	S_AppServiceSuccess	Download
                eventparts = strline.split('\t')
                if eventparts[1] == "HTTP" and eventparts[4].startswith("Download"):
                    if eventparts[3] == 'S_AppServiceRequest':
                        lasdlsize = 0
                        totalsize = 0
                    elif eventparts[3] == 'S_AppServiceConfirm':
                        starttime = curtime
                        httpnewloop = True
                    elif eventparts[3] == 'S_AppServiceSuccess':
                        # print("success ", strline)
                        endtime = curtime
                        trantimes = endtime - starttime
                        msecs = ((trantimes.seconds * 1000) + (trantimes.microseconds / 1000)) / 1000
                        print('starttime:{0}, endtime:{1}, transtimes:{2}, transizes:{3}'.format(starttime, endtime,
                                                                                                 msecs,
                                                                                                 totalsize))
                        (dir, ffile_name) = os.path.split(file_all_name)
                        linelist.append([ffile_name, starttime, endtime, msecs, totalsize * 8])

                        httpnewloop = False
                    else:
                        pass
                else:
                    pass

            strline = f.readline()

    return linelist


if __name__ == '__main__':
    file_path = r'F:\0001_workspace\01_待处理的问题\A-路网通\00_待解码数据\0000_TEMP\本周未完成工作\宁夏\统计汇总\上海http\联通'

    file_list = list_file(file_path, ".lte")

    http_info_list = []

    for file in file_list:
        print("start stat file --> [{0}]".format(file))
        file_http_info = decode_lte_http(file)
        http_info_list.extend(file_http_info)

    csv_path = os.path.join(file_path, "shanghai_http_stat.csv")
    # print(csv_path)
    myCSV = CsvOpt(csv_path, 'w')
    myCSV.write_csv_lines(http_info_list, ["文件名", '开始时间', '结束时间', '传输用时', '传输大小'])
    print('执行完毕！')

    openfile = input("is open file now! [y/n]")
    if openfile == 'y':
        os.startfile(csv_path)
    else:
        pass
