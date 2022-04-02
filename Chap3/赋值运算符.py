#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.02
"""

# 赋值运算符，运算顺序从右到左
a = 3+4
print(a)

# 链式赋值
a = b = c = 20
print(id(a))
print(id(b))
print(id(c))

# 参数赋值
a = 20
a += 30  # 相当于a=a+30
print(a)
a -= 10
print(a)
a *= 2
print(a)
print(type(a))
a /= 3
print(a)
print(type(a))
a //= 2
print(a)
print(type(a))
a %= 3
print(a)

# 系列解包赋值
a, b, c = 20, 30, 40
print(a, b, c)  # 左右变量数要对应

# 交换两个变量值

a, b = 10, 20
print('交换之前：', a, b)
a, b = b, a
print('交换之后：', a, b)