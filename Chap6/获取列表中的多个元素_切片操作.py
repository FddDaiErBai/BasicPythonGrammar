# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.05
"""

# 切片的结果是原列表片段的拷贝
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print('原列表:', lst[1:6:1])

lst2 = lst[1:6:1]
print('切的片段:', id(lst2))

print(lst[1:2])
print(lst[1:2:])  # 默认步长为1

print(lst[:6:2])  # 默认开始为0

print(lst[1::2])  # 默认结束为最后一个元素

print(lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2])