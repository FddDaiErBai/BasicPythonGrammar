# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""


class Student:
    native_pace = '吉林'

    def __init__(self, name, age):
        self.name = name  # self.name称为实体属性,进行了一个赋值操作,将局部变量的name的值赋给实体属性
        self.age = age

    # 实例方法

    def eat(self):
        print('学生在吃饭......')

    # 静态方法
    @staticmethod
    def method():  # 静态方法不允许写self
        print('我使用了staticmethod进行修饰,所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我使用了classmethof进行修饰,所以我是类方法')


# 类之外定义的称为函数,类之内定义的称为方法

def drink():
    print('喝水.')


# 类属性的使用方式
print(Student.native_pace)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_pace)
print(stu2.native_pace)

Student.cm()  # 类方法

Student.method()  # 静态方法