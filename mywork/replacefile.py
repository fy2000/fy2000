# -*- coding:utf-8 -*-

import os
import sys

areaorg = 'Area="'
areabytes = str.encode(areaorg)
rightQuotationChar = str.encode('"')


def replace_file(txtname: str, savedir: str):
    with open(txtname, 'rb') as f:
        fileContents = bytearray(f.read())
        for i in range(len(fileContents)):
            if fileContents[i: i + 6] == areabytes:
                tempbytes = fileContents[i + 6:i + 24]  # 24 max offset
                qpos = tempbytes.find(rightQuotationChar)
                if qpos > 0:
                    tempbytes = tempbytes[0: qpos]

                tempstr = tempbytes.decode()

                replacelen = len(tempstr)

                # start chenge x*0.6 round down
                numlist = [int(int(it) * 0.6) for it in tempstr.split(", ")]
                # reverse conversion
                tempstr = ', '.join([str(ie) for ie in numlist])
                tempbytes = str.encode(tempstr)
                # slice assignment
                fileContents[i + 6:i + 6 + replacelen] = tempbytes

        savefilename = os.path.join(savedir, os.path.basename(txtname))
        # save chenged contents to file
        with open(savefilename, 'wb') as wf:
            wf.write(fileContents)


# program enter
if len(sys.argv) != 3:
    print('input char error!')
else:
    print('start deal target dir -->[{}]'.format(sys.argv[1]))

    target_dir = sys.argv[1]
    save_dir = sys.argv[2]
    filelist = []
    for root, dirs, files in os.walk(target_dir):
        if not root.endswith('\\'):
            root += '\\'
        for filename in files:
            if (filename.endswith('.uim')):
                fileallname = root + filename
                filelist.append(fileallname)

    print('have {} files need to be deal...'.format(len(filelist)))

    print('start replace files...')

    for item in filelist:
        try:
            replace_file(item, save_dir)
        except IOError:
            print('file changed fail! --> {}'.format(item))
        else:
            print('file changed success! --> {}'.format(item))
