# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.02
"""

a, b = 10, 20
print('a>b吗?', a > b)  # False
print('a<b吗?', a < b)  # True
print('a<=b吗?', a <= b)  # True
print('a<=b吗?', a <= b)  # False
print('a==b吗?', a == b)  # False
print("a!=b吗?", a != b)  # True

# =为赋值运算符，==为比较运算符
# 一个变量由部分组成，标识，类型，值
# == 比较的是标识还是值? 比较的是值
# 比较对象的标识使用 is

a = 10
b = 10
print(a == b)  # True 说明值相等
print(a is b)  # True 说明id相等

# 以下代码没学过，后面会讲解

lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]

print(lst1 == lst2)  # 值 True
print(lst1 is lst2)  # id False
print(id(lst1))
print(id(lst2))
print(a is not b)  # False
