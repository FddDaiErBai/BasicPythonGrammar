# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

# key不可以重复,value可以重复
d = {'name': '李四', 'name': '张三'}  # key不允许重复
print(d)

d = {'name': '张三', 'nikname': '张三'}  # value不允许重复
print(d)

# 字典是无序的

# key必须是不可变对象

# 字典也可以根据需要动态地伸缩

# 字典会浪费较大的内存，是一种使用空间换时间的数据结构