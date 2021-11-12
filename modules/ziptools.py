# -*- coding: utf-8 -*-
from os import path
import zipfile


def zip_compress(srcfile, desfile):
    filepath, filename = path.split(srcfile)
    zip = zipfile.ZipFile(desfile, 'w', compression=zipfile.ZIP_DEFLATED)
    zip.write(srcfile, filename)
    zip.close()


def zip_uncompress(zipfilename, unzippath=None):
    filepath, filename = path.split(zipfilename)
    zip = zipfile.ZipFile(zipfilename)
    if unzippath is None:
        zip.extractall(filepath)
    else:
        zip.extractall(unzippath)
    zip.close()
