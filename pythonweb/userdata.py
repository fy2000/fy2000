# -*- coding: utf-8 -*-

from dbtools import get_info_from_db


def get_user_info(username: str):
    sql = f"select strcode, strpassword from tb_cfg_static_user_info where strcode = '{username}'"
    return get_info_from_db(sql)


if __name__ == '__main__':
    print(get_user_info("suqin"))
