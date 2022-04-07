# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.07
"""

s = 'Hello,Python'
print(s.replace('Python', 'Java'))
s1 = 'Hello,Python,Python,Python'
print(s1.replace('Python', 'Java', 2))  # 指定最大替换次数

# 将列表或元组中的字符串合并成一个字符串
lst = ['Hello', 'Java', 'Python']
print('|'.join(lst))
print(''.join(lst))

t = ('Hello', 'Python', 'Java')
print(''.join(t))

print('*'.join('Python'))