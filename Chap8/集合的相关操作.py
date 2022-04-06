# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

# 集合元素的判断操作
s = {10, 20, 30, 40, 50, 60}
print(10 in s)
print(100 in s)

# 集合元素的新增操作
s.add(80)  # add一次添加一个元素
print(s)

s.update({200, 300, 400})  # update()至少添加一个元素
print(s)

s.update([100, 23, 56])
s.update((23, 45, 67))
print(s)

# 集合元素的删除操作
s.remove(100)
print(s)
# s.remove(500) KeyError:500

s.discard(500)  # 不抛出异常
print(s)

s.pop()  # 一次删除任意一个元素,没有参数
print(s)

s.clear()  # 清空集合
print(s)