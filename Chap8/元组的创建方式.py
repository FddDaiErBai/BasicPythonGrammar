# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

# 使用()
t = ('Hello', 'world', 98)
print(t)
print(type(t))

t2 = 'Hello', 'world', 98  # 省略()
print(t2)
print(type(t2))

t2 = ('Hello',)  # 若元组中只含一种元素,逗号不能省略
print(t2)
print(type(t2))

# 使用内置函数tuple()
t1 = tuple(('Hello', 'world', 98))
print(t1)

# 空元组
t4 = ()
t5 = tuple()
print(t4, t5)