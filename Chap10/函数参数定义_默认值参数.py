# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def func(a, b=100):  # b为默认参数值
    print(a, b)


func(10)
func(10, 20)

print('Hello', end='\t')
print('world')