# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

from unicodedata import name


class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行,cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象id为{0}'.format(id(obj)))
        return obj

    def __init__(self, nama, age):
        print('__init__被调用,self的ID值为{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object这个类对象的id为{0}'.format(id(object)))
print('Person这个类对象的id为{0}'.format(id(Person)))

# 创建Person类的实例对象

p1 = Person('张三', 20)
print('p1这个Person类的实例对象的id为{0}'.format(id(p1)))