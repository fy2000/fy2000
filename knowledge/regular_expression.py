# -*- coding:utf-8 -*-
import re

if __name__ == '__main__':
    line = "he is arat, he is in a rut, the food is Rotten, I like root beer."

    # mathobj = re.search(r'(.*)oo(.*?) .*', line, re.M | re.I)
    #
    # print(mathobj.group())
    # print(mathobj.group(1))
    # print(mathobj.group(2))

    phone = "2004-959-559 # 这是一个国外电话号码"

    # 删除字符串中的 Python注释
    num = re.sub(r'一.*$', "", phone)
    print("电话号码是: ", num)

    # 删除非数字(-)的字符串
    num = re.sub(r'\D', "", phone)
    print("电话号码是 : ", num)
