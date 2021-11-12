# -*- coding: utf-8 -*-
from fyfunc import Teacher, Student


def print_teacher_info():
    name = input("请输入老师的名字：")
    subject = input("请输入老师教的学科：")
    teacher = Teacher(name, subject)
    teacher.run()


def print_student_info():
    name = input("请输入学生的名字：")
    subject = int(input("请输入学生的年龄："))
    stu = Student(name, subject)
    stu.run()


def main_menu():
    while True:
        print("请输入功能序号：\n 1.输出老师信息\n 2.输出学生信息\n 3.退出")
        num = int(input("请输入您的选择："))
        if num == 1:
            print_teacher_info()
        elif num == 2:
            print_student_info()
        elif num == 3:
            break
        else:
            print("输入错误，请重新输入...")


if __name__ == '__main__':
    main_menu()
