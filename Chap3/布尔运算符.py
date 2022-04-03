# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.02
"""

# 布尔运算符

# and
a, b = 1, 2
print(a == 1 and b == 2)  # True
print(a == 1 and b < 2)  # False
print(a != 1 and b == 2)  # False
print(a != 1 and b != 2)  # False

# or
print(a == 1 or b == 2)  # True
print(a == 1 or b < 2)  # True
print(a != 1 or b == 2)  # True
print(a != 1 or b != 2)  # False

# not
f = True
f2 = False
print(not f)
print(not f2)

# in
s = 'Hello,world'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
