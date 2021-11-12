# -*- coding: utf-8 -*-

from modules.opsqlite import SqliteOpt


def get_info_from_db(sql: str):
    sqlt = SqliteOpt('../MBDatabase/mbdata.db')
    reqinfo = sqlt.search(sql)
    sqlt.close()
    return reqinfo


if __name__ == '__main__':
    sumnum = 0
    print("总和", sumnum)
