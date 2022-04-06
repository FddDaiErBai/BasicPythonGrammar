# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

t = ('Hello', 'world', 98)

# 使用索引
print(t[0])
print(t[1])
print(t[2])
# print(t[3]) IndexError:tuple index out of range

# 遍历元组
for item in t:
    print(item)