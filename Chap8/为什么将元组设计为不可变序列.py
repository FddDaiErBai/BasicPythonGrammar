# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

# 在多任务环境下,同时操作对象时不需要加锁
# 在程序中尽量使用不可变序列

# 元组存储的是数据的引用
t1 = (9, [20, 30], 10)
print(t1)
print(type(t1))
print(t1[0], type(t1[0]), id(t1[0]))
print(t1[1], type(t1[1]), id(t1[1]))

# 试图将t[1]修改为100
# t1[1]=100 元组不允许修改元素

# 由于列表是可变序列,可以向中添加元素,列表的内存地址不变
t1[1].append(100)
print(t1)
print(id(t1[1]))