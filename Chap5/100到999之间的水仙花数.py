# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

for item in range(100, 1000):
    ge = item % 10
    shi = item//10 % 10
    bai = item//100
    if ge**3+shi**3+bai**3 == item:
        print(item)
