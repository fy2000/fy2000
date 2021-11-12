# -*- coding: utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from configsetting import ConfigSetting
from cuspaymentinfo import CusPaymentInfo
from annualsalesinfo import AnnualSalesInfo
from receivableorderinfo import ReceivableOrderInfo

if __name__ == '__main__':
    cfgfile = os.path.join(curPath, 'fy2000.ini')
    cfg = ConfigSetting(cfgfile)
    dbfile = os.path.join(curPath, cfg.dbname)

    cpi = CusPaymentInfo(cfg.cus_payment_file_path, dbfile)
    cpi.read_file()
    cpi.save2db()

    cpi = AnnualSalesInfo(cfg.annual_sales_file_path, dbfile)
    cpi.read_file()
    cpi.save2db()

    cpi = ReceivableOrderInfo(cfg.receivable_order_file_path, dbfile)
    cpi.read_file()
    cpi.save2db()
