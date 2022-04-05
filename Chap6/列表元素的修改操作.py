# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.05
"""

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 一次修改一个元素
lst[2] = 100
print(lst)

# 修改多个值
lst[1:3] = [300, 500, 600]
print(lst)