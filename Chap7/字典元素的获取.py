# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

# 获取字典中的元素
scores = {'张三': 100, '李四': 8, '王五': 45}

# 使用[]
print(scores['张三'])
# print(scores['陈六']) KeyError:'陈六'

# 使用get()方法
print(scores.get('张三'))
print(scores.get('陈六'))  # None
print(scores.get('麻七'), 99)  # 查找建不存在,返回提供的默认值