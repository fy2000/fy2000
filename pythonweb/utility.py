# -*- coding: utf-8 -*-

from pythonweb import userdata, monthdim


def get_user_info(username: str):
    return userdata.get_user_info(username)


def get_month_info():
    return monthdim.get_month_info()


def get_cus_info():
    return monthdim.get_month_info()

if __name__ == '__main__':
    # print(sys.path)
    for item in get_user_info("suqin"):
        print(item)
