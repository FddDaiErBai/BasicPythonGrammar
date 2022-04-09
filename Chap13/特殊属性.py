# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

# print(dir(object))


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建C类的对象
x = C('Jack', 20)  # x是C类的一个实例对象

print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)

print(x.__class__)  # 对象所属的类

print(C.__bases__)  # C类的父类类型的元组

print(C.__base__)  # 类的基类(最近的类)

print(C.__mro__)  # 类的结构层次

print(A.__subclasses__())  # 子类的列表