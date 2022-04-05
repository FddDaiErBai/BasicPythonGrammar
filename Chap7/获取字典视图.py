# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

scores = {'张三': 100, '李四': 8, '王五': 45}
# 获取所有的key
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有key组成的视图转成列表

# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))

# 获取所有的key-value对 ()是元组类型
items = scores.items()
print(items)
print(type(items))
print(list(items))