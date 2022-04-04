# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

lst = ['Hello', 'world', 98, 'Hello']
print(lst.index('Hello'))  # 如果列表存在相同元素,只返回相同元素的第一个元素的索引

print(lst.index('Hello', 1, 4))  # 指定范围

print(lst.index('python'))  # ValueError 不存在查找元素