# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

# 输出1到50之间所有5的倍数
for item in range(1, 51):
    if item % 5 == 0:
        print(item)

# 使用continue

for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)