# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

from re import A


sum = 0
a = 1

while a <= 100:
    if a % 2 == 0:
        sum += a
    a += 1
print('1-100的偶数和:', sum)
