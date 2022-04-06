# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

s = 'Hello,python'
a = s.upper()  # 将所有字母转换成大写,会产生一个新的字符串对象
print(a, id(a))
print(s, id(s))

b = s.lower()
print(b, id(b))  # 将所有字母转换成小写,会产生一个新的字符串对象
print(s, id(s))
print(b == s)
print(b is s)

s2 = 'Hello,Python'
print(s2.swapcase())  # 大写变小写，小写变大写

print(s2.title())  # 每一个单词首字母大写