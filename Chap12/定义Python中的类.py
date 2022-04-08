# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""


class Class:  # Class为类的名称(类名)由一个或多个单词组成,每个单词的首字母大写,其余小写
    pass  # 占位


# Python中一切皆对象,Class是对象吗?内存有开空间吗?
print(id(Class))
print(type(Class))
print(Class)


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
    def cm():
        print('我使用了classmethof进行修饰,所以我是类方法')


# 类之外定义的称为函数,类之内定义的称为方法

def drink():
    print('喝水.')