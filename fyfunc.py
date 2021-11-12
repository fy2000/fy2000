# -*- coding: utf-8 -*-

class Grade:  # 年级类
    def __init__(self):
        self.g_grade = "三年级"

    def __str__(self):
        return self.g_grade


class Class:  # 班级类
    def __init__(self):
        self.c_class = "1001班"

    def __str__(self):
        return self.c_class


class Teacher(Grade, Class):
    def __init__(self, name, subject):
        Grade.__init__(self)
        Class.__init__(self)
        self.t_name = name
        self.t_subject = subject

    def run(self):
        print("\n我是一名老师\n名字：%s\n在%s%s教%s课\n"
              % (self.t_name, self.g_grade, self.c_class, self.t_subject))


class Student(Grade, Class):
    def __init__(self, name, age):
        Grade.__init__(self)
        Class.__init__(self)
        self.s_name = name
        self.s_age = age

    def run(self):
        print("\n我叫%s\n今年%d岁了\n在%s%s上课\n"
              % (self.s_name, self.s_age, self.g_grade, self.c_class))
