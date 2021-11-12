# -*- coding: utf-8 -*-
import configparser


class ConfigSetting:
    def __init__(self, inifile: str):
        cfgp = configparser.ConfigParser()
        cfgp.read(inifile, encoding='utf-8')
        self.cus_payment_file_path = cfgp.get(configparser.DEFAULTSECT, 'cus_payment_file_path')
        self.annual_sales_file_path = cfgp.get(configparser.DEFAULTSECT, 'annual_sales_file_path')
        self.receivable_order_file_path = cfgp.get(configparser.DEFAULTSECT, 'receivable_order_file_path')

        self.dbname = cfgp.get('DBINFO', 'dbbname')
        print('加载配置信息成功...')


if __name__ == "__main__":
    cg = ConfigSetting("fy2000.ini")

