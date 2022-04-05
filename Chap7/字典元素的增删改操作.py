# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

scores = {'张三': 100, '李四': 8, '王五': 45}

# 字典元素的判断
print('张三' in scores)
print('张三' not in scores)

# 字典元素的删除
del scores['张三']  # 删除指定的key-value对
# scores.clear() 清空字典元素
print(scores)

# 添加字典元素
scores['陈六'] = 98
print(scores)

# 修改字典元素
scores['陈六'] = 100
print(scores)