# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

# 元组是python内置函数之一,是一个不可变序列

# 可变序列,地址不发生改变
lst = [1, 2, 3, 4, 5]
print(id(lst))
lst.append(3)
print(id(lst))

# 不可变序列,地址发生改变
s = 'Hello'
print(id(s))
s += 'world'
print(id(s))