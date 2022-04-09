# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

from math import pi
import math  # 关于数学运算
# 如何导入自定义模块
from calc import add
import calc

print(id(math))
print(type(math))
print(math)

print(math.pi)
print(dir(math))

print(math.pow(2, 3), type(math.pow(2, 3)))
print(math.ceil(9.001))
print(math.floor(9.999))

print(pi)