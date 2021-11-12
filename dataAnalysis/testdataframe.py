# -*- coding: utf-8 -*-
from pandas import DataFrame


class StudentDf:
    def __init__(self):
        testdict1 = {
            '编号': ['1', '2', '3', '4'],
            '姓名': ['小红', '小明', '小丽', '小刚'],
            '性别': ['女', '男', '女', '男'],
            '年龄': [21, 34, 12, 35]
        }

        self.df = DataFrame(testdict1)


class TeacherDf:
    def __init__(self):
        testdict1 = {
            '姓名': ['李老师', '王老师', '郭老师', '于老师'],
            '性别': ['男', '男', '男', '女'],
            '年龄': [45, 34, 34, 54]
        }

        self.df = DataFrame(testdict1)


class FoodDf:
    def __init__(self):
        fdict1 = {
            '编号': ['00', '01', '02', '03'],
            '名称': ['方便面', '香蕉', '辣条', '鸡蛋'],
            '单价': [1, 5, 3.5, 7]
        }

        self.df = DataFrame(fdict1)


if __name__ == '__main__':
    df = TeacherDf().df
    print(df)
