# -*- coding: utf-8 -*-
from emailopt import EmailOpt          # 导入邮件操作类模块

if __name__ == "__main__":
    e_addr = input("请输入您的邮箱账号：")
    e_pwd = input("请输入您的邮箱密码：")
    d_addr = input("请输入收件人邮箱地址：")
    e_data = input("请输入您要发送的内容：")

    e_opt = EmailOpt(e_addr, e_pwd)     # 创建邮件操作类
    e_opt.set_destination_info(d_addr)  # 设置收件人邮箱地址
    e_opt.set_send_data(e_data)         # 设置发送的邮件内容
    e_opt.set_header_info("休假通知")     # 设置邮件标题
    if e_opt.send_email():              # 执行邮件发送任务，并返回成功和失败
        print("邮件发送成功！")
    else:
        print("邮件发送失败！")
