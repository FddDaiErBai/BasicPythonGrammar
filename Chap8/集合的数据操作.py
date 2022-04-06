# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

# 交集操作
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 60}
print(s1.intersection(s2))
print(s1 & s2)  # intersection()与 & 等价,交集操作

print(s1)
print(s2)

# 并集操作
print(s1.union(s2))
print(s1 | s2)  # union()与 | 等价,并集操作

print(s1)
print(s2)

# 差集操作
print(s1.difference(s2))
print(s1-s2)  # difference()与 - 等价,差集操作

print(s1)
print(s2)

# 对称差集操作
print(s1.symmetric_difference(s2))
print(s1 ^ s2)  # symmetric_difference()与 ^ 等价,对称差集操作