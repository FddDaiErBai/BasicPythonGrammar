# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

# 一个py文件就是一个模块


def func():
    pass


class Student:
    native_palce = '吉林'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        pass

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass


a = 10
b = 20
print(a+b)