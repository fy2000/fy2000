# -*- coding: utf-8 -*-
import string
import random
import math
from operator import *


# 是否为负的小数
def is_negative_float(element):
    str_num = str(element)
    if str_num.count('.') == 1:
        num_part = str_num.split('.')
        left = num_part[0]
        right = num_part[1]
        if right.isdigit():
            if left.count('-') == 1 and left.startswith('-'):
                num = left[1:]
                if num.isdigit():
                    return True
    return False


# 是否为正的小数
def is_positive_float(element):
    str_num = str(element)
    if str_num.count('.') == 1:
        num_part = str_num.split('.')
        left = num_part[0]
        right = num_part[1]
        if right.isdigit():
            if left.isdigit():
                return True
    return False


# 是否为负整数
def is_negative_int(element):
    str_num = str(element)
    if str_num.count('-') == 1 and str_num.startswith('-'):
        num = str_num[1:]
        if num.isdigit():
            return True
    return False


# 是否为正整数
def is_positive_int(element):
    str_num = str(element)
    if str_num.isdigit():
        return True
    else:
        return False


# 是否为正数
def is_positive_digit(element):
    if is_positive_int(element) or is_positive_float(element):
        return True
    else:
        return False


# 是否为负数
def is_negative_digit(element):
    if is_negative_int(element) or is_negative_float(element):
        return True
    else:
        return False


# 是否为数字
def is_digit(element):
    if is_positive_digit(element) or is_negative_digit(element):
        return True
    else:
        return False


# 获取随机验证码，参数为验证码位数
def random_verification_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ""
    for i in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def random_code(code_len=4):
    code_list = string.digits + string.ascii_letters
    result_list = random.sample(code_list, code_len)
    code = ''.join(result_list)
    return code


# 求多个列表的最大值 [[1, 2, 3], [4, 9, 7], [8, 5]] 返回 9
def max_lists(*lst):
    return max(max(*lst, key=lambda v: max(v)))


# 不适用if else 实现简单计算器
def calculator(a, b, k):
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '**': pow
    }.get(k, add)(a, b)


# 利用海伦公式计算三角形面积 参数为三角形三条边
def triangle_area(a, b, c):
    area = 0
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return area


# 最⼤公约数
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


# 最⼩公倍数
def lcm(x, y):
    return x * y // gcd(x, y)


# 九九乘法表
def multiplication_table():
    _99cfb = '\n'.join(['\t'.join('%dx%d=%2d' % (x, y, x * y) for x in range(1, y + 1)) for y in range(1, 10)])
    return _99cfb


# 判断一个数是否为水仙花数
def is_narcissistic_num(num):
    number = str(num).strip()
    mi = len(number)
    if mi < 3:
        raise ValueError("The number of digits is less than 3")
    mi = len(number)
    bw = int(number[0])
    sw = int(number[1])
    gw = int(number[2])

    if int(num) == bw ** mi + sw ** mi + gw ** mi:
        return True
    else:
        return False


# 判断指定的年份是不是闰年
# :param year: 年份
# :return: 闰年返回True平年返回False
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def bubble_sort(li):
    for i in range(len(li)-1):
        swapped = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                swapped = True
        if not swapped:
            break


