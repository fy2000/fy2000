# -*- coding: utf-8 -*-
import datetime
import csv

if __name__ == '__main__':
    file_path = r'F:\0001_workspace\01_待处理的问题\A-路网通\00_待解码数据\0000_TEMP\本周未完成工作\辽宁\网格16\2402451820210824101509MS1.l5g'

    datedic = {}
    starttime = datetime.datetime.now()
    endtime = datetime.datetime.now()
    curtime = datetime.datetime.now()

    lasdlsize = 0
    ftpDownloadTransSize = 0.0
    linelist = []
    ttime = []
    tsize = []
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
                curtime = datetime.datetime(datedic['year'], datedic['month'], datedic['day'], datedic['hour'], datedic['min'], datedic['sec'], datedic['msec']*1000)
                # print(curtime)
            elif strline.startswith('APPLAYER'):
                # APPLAYER FTP   20341004.921875#20341004.921875#################854548.361000#
                layerparts = strline.split('\t')
                speeds = layerparts[3].split('#')
                tranSize = float(speeds[9])
                # ftpDownloadTransSize = (tranSize - lasdlsize) * 1024
                # lasdlsize = tranSize
                ftpDownloadTransSize = tranSize * 1024
                # print(ftpDownloadTransSize)
            elif strline.startswith('APPEVENT'):
                # APPEVENT FTP 10000001-1-1629807021-1 S_APPServiceConfirm
                eventparts = strline.split('\t')
                if eventparts[3] == 'S_APPServiceConfirm':
                    starttime = curtime
                elif eventparts[3] == 'S_APPServiceSuccess':
                    endtime = curtime
                    trantimes = endtime - starttime
                    msecs = ((trantimes.seconds * 1000) + (trantimes.microseconds / 1000)) / 1000
                    print('starttime:{0}, endtime:{1}, transtimes:{2}, transizes:{3}'.format(starttime, endtime, msecs, ftpDownloadTransSize))
                    # print(type(ftpDownloadTransSize))
                    ttime.append(msecs)
                    tsize.append(float(ftpDownloadTransSize))
                    linelist.append([starttime, endtime, msecs, ftpDownloadTransSize])
                    ftpDownloadTransSize = 0

                    # break
            strline = f.readline()

    with open(r'F:\0001_workspace\01_待处理的问题\A-路网通\00_待解码数据\0000_TEMP\本周未完成工作\辽宁\网格16\2402451820210824101509MS1.csv', 'a', newline='') as r:
        writer = csv.writer(r)
        sumtime = sum(ttime)
        sumsize = sum(tsize)
        avgspeed = (sumsize / sumtime) * 8 / 1000 / 1000
        writer.writerow(['starttime', 'endtime', 'usetime', 'transsize'])
        for item in linelist:
            writer.writerow(item)

        writer.writerow([sumtime, sumsize, avgspeed, 0])

    print('执行完毕！')