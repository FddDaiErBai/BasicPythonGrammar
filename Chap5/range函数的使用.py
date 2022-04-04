# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

# range的三种创建方式

r = range(10)  # 默认从0开始，默认步长为1
print(r)  # range(0，10)
print(list(r))  # 用于查看range对象中的整数序列 list是列表

r = range(1, 10)  # 从1开始到10结束，不含10，默认步长为1
print(list(r))

r = range(1, 10, 2)
print(list(r))  # 从1开始到10结束，不含10，步长为2

# 判断指定的整数是否在序列中 in not in

print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)

# 存储个数不同，内存空间相等，不用不计算
print(range(1, 20, 1))
print(range(1, 101, 1))