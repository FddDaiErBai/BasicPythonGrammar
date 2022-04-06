# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

# 集合是可变序列
# 集合时没有value的字典

# 使用{}
s = {2, 3, 4, 5, 5, 6, 7, 7}  # 集合中的元素不能重复
print(s)

# 使用内置函数set()
s1 = set(range(6))
print(s1, type(s1))

s2 = set([1, 2, 3, 4, 5, 5, 5, 6, 6])
print(s2, type(s2))

s3 = set((1, 2, 3, 44, 5, 65))  # 集合中的元素是无序的
print(s3, type(s3))

s4 = set(('Python'))
print(s4, type(s4))

s5 = set({2, 32, 5, 3, 43})
print(s5, type(s5))

# 定义一个空集合
s6 = {}  # dict字典类型
print(s6, type(s6))

s7 = set()
print(s7, type(s7))