# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.07
"""

# 字符串是不可变类型
# 不具备增删改等操作
# 切片将产生新的对象

s = 'Hello,Pytohn'
s1 = s[:5]  # 没有起始位置,默认0开始
s2 = s[6:]  # 没有结束位置,默认末尾结束
s3 = '!'
new_s = s1+s3+s2

print(s1)
print(s2)
print(new_s)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(new_s))

# 完整写法 [start:end:step]
print(s[1:5:1])
print(s[::2])
print(s[::-1])
print(s[-6::])