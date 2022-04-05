# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

scores = {'张三': 100, '李四': 8, '王五': 45}

# 字典元素的遍历
for item in scores:
    print(item, scores[item], scores.get(item))