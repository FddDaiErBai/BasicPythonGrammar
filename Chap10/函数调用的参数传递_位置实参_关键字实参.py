# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def calc(a, b):  # a,b称为形式参数,简称形参,形参的位置是在函数的定义处
    c = a+b
    return c


# 位置参数
result = calc(10, 20)  # 10,20称为实际参数的值,简称实参,实参的位置是在函数的调用处
print(result)

res = calc(b=10, a=20)  # =左边的变量名称为关键字参数
print(res)