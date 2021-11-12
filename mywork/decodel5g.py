# -*- coding: utf-8 -*-
import datetime
import csv
import sys
import os


def decode_l5g_file(file_path: str, linelist: list):
    datedic = {}

    tempdic = {}

    with open(file_path, 'r') as f:
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
            elif strline.startswith('APPEVENT'):
                # APPEVENT  Protocol   ESN  EName   EInfo
                eventparts = strline.split('\t')
                if (eventparts[1] == "PING") and (eventparts[3] == "S_APPServiceRequest"):  # ping 请求
                    tempdic['starttime'] = curtime
                    tempdic['event_s'] = eventparts[3]
                elif (eventparts[1] == "PING") and (eventparts[3] == "S_APPServiceSuccess"):  # ping 响应
                    endtime = curtime
                    offsettime = endtime - tempdic['starttime']
                    msecs = (offsettime.seconds * 1000) + (offsettime.microseconds / 1000)
                    # print([tempdic['starttime'], tempdic['event_s'], endtime, eventparts[3], msecs])
                    linelist.append([tempdic['starttime'], tempdic['event_s'], endtime, eventparts[3], msecs])
                    # break
            strline = f.readline()


def write_csv_file(file_path: str, linelist: list):
    new_path = file_path + '.csv'
    with open(new_path, 'a', newline='') as w:
        writer = csv.writer(w)
        writer.writerow(['starttime', 'event_s', 'endtime', 'event_e', 'offsettime'])
        for item in linelist:
            writer.writerow(item)


def docode_file_2_csv(fitem):
    linelist = []
    # 解析文件
    decode_l5g_file(fitem, linelist)

    # 保存文件
    write_csv_file(fitem, linelist)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('input char error!')
    else:
        print('start deal target dir -->[{}]'.format(sys.argv[1]))

        target_dir = sys.argv[1]
        filelist = []
        for root, dirs, files in os.walk(target_dir):
            if not root.endswith('\\'):
                root += '\\'
            for filename in files:
                if filename.endswith('.l5g'):
                    fileallname = root + filename
                    filelist.append(fileallname)

        print('have {} files need to be deal...'.format(len(filelist)))

        print('start decode files...')

        for fitem in filelist:
            try:
                docode_file_2_csv(fitem)
            except IOError:
                print('file changed fail! --> {}'.format(fitem))
            else:
                oldpath, oldfname = os.path.split(fitem)
                print('file decode success! --> {}'.format(oldfname))
