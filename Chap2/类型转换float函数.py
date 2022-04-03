# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.02
"""

print('---------float函数将其他类型转成float类型-----------')
s1 = '128.98'
s2 = '76'
ff = True
s3 = 'Hello'
i = 98

print(type(s1), type(s2), type(ff), type(s3), type(i))

print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
print(float(ff), type(float(ff)))
# print(float(s3), type(float(s3))) #字符串如果是非字符串，则不允许转换
print(float(i), type(float(i)))
