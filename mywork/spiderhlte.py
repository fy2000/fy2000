# -*- coding: utf-8 -*-
import datetime
import csv
import sys
import os

ncelllist = []  # 用来存储 邻区 的行
linelist = []  # 用来存储 输出信息 的行


def decode_hhltenc(ncParts: list, scDic: dict):
    # RegReport	HHLTENC	Neighbour_Cell_Count	PCI	RSRP	RSRQ	RSSI	EARFCN	distance	SINR
    groupCount = int(ncParts[1]) if ncParts[1] != "" else 0
    pciParts = ncParts[2].split(" ")
    rsrpParts = ncParts[3].split(" ")
    rsrqParts = ncParts[4].split(" ")
    earfcnParts = ncParts[6].split(" ")

    for i in range(groupCount):
        ncDic = {'longitude': scDic['longitude'], 'latitude': scDic['latitude'],
                 'earfcn': float(earfcnParts[i]) if earfcnParts[i] != "" else '',
                 'pci': int(pciParts[i]) if pciParts[i] != "" else '', 'eci': "",
                 'rsrp': float(rsrpParts[i]) if rsrpParts[i] != "" else '',
                 'rsrq': float(rsrqParts[i]) if rsrqParts[i] != "" else '', 'Altitude': '', 'NorthShift': '',
                 'EastShift': '', 'HeightShift': "", 'Version': "", 'MapX': "", 'MapY': "", 'celltype': 'NCell'}

        ncelllist.append(ncDic)


def decode_hhgyro(gpsParts: list, scDic: dict):
    # HHGYRO	LastLongitude	LastLatitude	LastAltitude	NorthShift	EastShift	HeightShift	Version MapX MapY
    scDic['longitude'] = float(gpsParts[1]) if gpsParts[1] != "" else scDic['longitude']
    scDic['latitude'] = float(gpsParts[2]) if gpsParts[2] != "" else scDic['latitude']
    scDic['Altitude'] = float(gpsParts[3]) if gpsParts[3] != "" else scDic['Altitude']
    scDic['NorthShift'] = float(gpsParts[4]) if gpsParts[4] != "" else scDic['NorthShift']
    scDic['EastShift'] = float(gpsParts[5]) if gpsParts[5] != "" else scDic['EastShift']
    scDic['HeightShift'] = float(gpsParts[6]) if gpsParts[6] != "" else scDic['HeightShift']
    scDic['Version'] = float(gpsParts[7]) if gpsParts[7] != "" else scDic['Version']
    scDic['MapX'] = float(gpsParts[8]) if gpsParts[8] != "" else scDic['MapX']
    scDic['MapY'] = float(gpsParts[9]) if gpsParts[9] != "" else scDic['MapY']


def decode_hhltenwi(nwiParts: list, scDic: dict):
    # RegReport	HHLTENWI	PCI	BandWidth_DL	Special_SubFrame_Patterns	SubFrame_Allginment_Type
    # Frequency_DL	EARFCN_DL	BandWidth_UL	Frequency_UL	Work_Mode	Band	CP_Type	EARFCN_UL
    # OFDM_Symbols_Number	EMM_State	EMM_Sub_State	EMM_Update	Feasure_Group_Indicators	MME_Code
    # MME_Group_ID	MCC	MNC	RRC_Protocol	LTETechnology	CAIndex
    scDic['pci'] = int(nwiParts[1]) if nwiParts[1] != "" else scDic['pci']
    scDic['earfcn'] = int(nwiParts[6]) if nwiParts[6] != "" else scDic['earfcn']


def decode_hhltesc(scParts: list, scDic: dict):
    # HHLTESC	SINR	Rank_Indicator	Rank1_SINR	Rank2_SINR1	Rank2_SINR2	RSRP
    # RSRQ	RSSI	ECGI	RSRP_Rx0	RSRP_Rx1	Transmission_Mode	ECI	CRS_SINR	DRS_SINR
    # CRS_RP	DRS_RP	Frame_Number	SubFrame_Number	TTI_Count	MIMO_MultiUser_Indicator
    # eNb_Tx_Antenna_Num	Cell_Allowed_Access	Cell_Barred	Cell_Reserved	TAC	RSRQ_Rx0	RSRQ_Rx1
    # RSSI_Rx0	RSSI_Rx1	SINR_Rx0	SINR_Rx1	Pathloss	CellID	CAIndex
    scDic['rsrp'] = float(scParts[6]) if scParts[6] != "" else scDic['rsrp']
    scDic['rsrq'] = float(scParts[7]) if scParts[7] != "" else scDic['rsrq']
    scDic['eci'] = int(scParts[13]) if scParts[13] != "" else scDic['eci']


def decode_sec(minparts: list, scDic: dict):
    scDic['sec'] = int(minparts[1])
    scDic['msec'] = int(minparts[2])
    curtime = datetime.datetime(scDic['year'], scDic['month'], scDic['day'], scDic['hour'],
                                scDic['min'], scDic['sec'], scDic['msec'] * 1000)
    linelist.append(
        [curtime, scDic['longitude'], scDic['latitude'], scDic['Altitude'], scDic['NorthShift'],
         scDic['EastShift'], scDic['HeightShift'], scDic['Version'], scDic['MapX'], scDic['MapY'],
         scDic['earfcn'], scDic['pci'], scDic['eci'], scDic['rsrp'], scDic['rsrq'], scDic['celltype']])

    for ncitem in ncelllist:
        linelist.append(
            [curtime, ncitem['longitude'], ncitem['latitude'], ncitem['Altitude'], ncitem['NorthShift'],
             ncitem['EastShift'], ncitem['HeightShift'], ncitem['Version'], ncitem['MapX'], ncitem['MapY'],
             ncitem['earfcn'], ncitem['pci'], ncitem['eci'], ncitem['rsrp'], ncitem['rsrq'],
             ncitem['celltype']])
    ncelllist.clear()


def decode_min(minparts: list, scDic: dict):
    scDic['min'] = int(minparts[1])


def decode_hour(hourparts: list, scDic: dict):
    scDic['hour'] = int(hourparts[1])


def decode_day(dayparts: list, scDic: dict):
    scDic['year'] = int(dayparts[1])
    scDic['month'] = int(dayparts[2])
    scDic['day'] = int(dayparts[3])


def decodefile(file_path: str):
    scDic = {'longitude': "", 'latitude': '', 'earfcn': "", 'pci': "", 'eci': "", 'rsrp': "", 'rsrq': "",
             'Altitude': '', 'NorthShift': '', 'EastShift': '', 'HeightShift': "", 'Version': "", 'MapX': "",
             'MapY': "", 'celltype': 'SCell'}

    decode_fun = {'DAY': decode_day,
                  'HOUR': decode_hour,
                  'MIN': decode_min,
                  'SEC': decode_sec,
                  'HHLTESC': decode_hhltesc,
                  'HHLTENWI': decode_hhltenwi,
                  'HHGYRO': decode_hhgyro,
                  'HHLTENC': decode_hhltenc,
                  }

    with open(file_path, 'r') as f:
        strline = f.readline()
        while strline:
            dataParts = strline.split('\t')
            if dataParts[0] in decode_fun.keys():
                decode_fun[dataParts[0]](dataParts, scDic)

            strline = f.readline()


def write_csvfile(file_path: str):
    new_path = file_path + '.csv'
    with open(new_path, 'w+', newline='') as r:
        writer = csv.writer(r)
        writer.writerow(
            ['time', 'longitude', 'latitude', 'Altitude', 'NorthShift', 'EastShift', 'HeightShift', 'Version', 'MapX',
             'MapY', 'earfcn', 'pci', 'eci', 'rsrp', 'rsrq', 'celltype'])
        for item in linelist:
            writer.writerow(item)


def docodefile2csv(file_path: str):
    # 解析原始文件
    decodefile(file_path)

    # 将解码后的数据写入csv文件
    write_csvfile(file_path)


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
                if filename.endswith('.hlte'):
                    fileallname = root + filename
                    filelist.append(fileallname)

        print('have {} files need to be deal...'.format(len(filelist)))

        print('start decode files...')

        for fitem in filelist:
            try:
                docodefile2csv(fitem)
            except IOError:
                print('file changed fail! --> {}'.format(fitem))
            else:
                oldpath, oldfname = os.path.split(fitem)
                print('file decode success! --> {}'.format(oldfname))
