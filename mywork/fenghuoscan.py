# -*- coding:utf-8 -*-
import os
import sys
import datetime


def unpacket_file(file_name):
    f_bak = open(file_name + '.bak', 'w')

    with open(file_name, 'rb') as f:
        p_data = f.read(15)
        fh_flag = p_data[:9].decode("utf-8")
        # print(fh_flag)
        if fh_flag != "FH-R-3001":
            print('this file is not 烽火扫频文件! ...')
            return

        fh_day = int.from_bytes(p_data[9:10], byteorder='little')
        fh_month = int.from_bytes(p_data[10:11], byteorder='little')
        fh_year = int.from_bytes(p_data[11:13], byteorder='little')

        fh_nettype = int.from_bytes(p_data[13:15], byteorder='little')

        f_bak.write("{0} nettype = {1}\n".format(fh_flag, fh_nettype))

        while True:
            p_data = f.read(20)
            # print(p_data)
            if p_data == b'':
                break

            fh_msec = int.from_bytes(p_data[:2], byteorder='little') & 1023
            fh_sec = (p_data[1] >> 2) & 63
            fh_min = (p_data[2] & 63)
            fh_hour = (int.from_bytes(p_data[2:4], byteorder='little') >> 6) & 31
            fh_datatime = "{0}-{1}-{2} {3}:{4}:{5}.{6}".format(fh_year, fh_month, fh_day, fh_hour, fh_min, fh_sec,
                                                               fh_msec)

            net_symbol1 = int.from_bytes(p_data[4:8], byteorder='little')
            net_symbol2 = int.from_bytes(p_data[8:12], byteorder='little')

            datalen = int.from_bytes(p_data[16:20], byteorder='big')
            p_data += f.read(datalen)
            w_line_data = "0x{0:08x}-0x{1:08x} {2} {3}\n".format(net_symbol1, net_symbol2, fh_datatime, p_data.hex(' '))
            f_bak.write(w_line_data)
            # print(w_line_data)

            # break
        f_bak.close()


if __name__ == "__main__":
    target_file = ""

    if len(sys.argv) != 2:
        print('use test file path!...')
        target_file = "F:\\0001_workspace\\01_待处理的问题\\A-路网通\\00_待解码数据\\0000_TEMP\\本周未完成工作\\四川\\扫频测试_区县\\" \
                      "区县网格_德阳绵竹市_20211030_NR"
    else:
        target_file = sys.argv[1]

    print('start deal target dir -->[{}]'.format(target_file))
    if target_file:
        print('start unpacket file...')

        try:
            unpacket_file(target_file)
        except IOError:
            print('file unpacket fail! --> {}'.format(target_file))
        else:
            oldpath, oldfname = os.path.split(target_file)
            print('file unpacket success! --> {}'.format(oldfname))
    else:
        print("file name is empty!...")
