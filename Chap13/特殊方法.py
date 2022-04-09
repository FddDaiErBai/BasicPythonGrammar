# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

a = 20
b = 100
c = a+b
d = a.__add__(b)

print(c)
print(d)


class A:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)


stu1 = A('张三')
stu2 = A('李四')

s = stu1+stu2  # 实现两个对象的加法运算(编写__add__方法)

print(s)

s = stu1.__add__(stu2)
print(s)

lst = [11, 22, 33, 44]
print(len(lst))
print(lst.__len__())

print(len(stu1))