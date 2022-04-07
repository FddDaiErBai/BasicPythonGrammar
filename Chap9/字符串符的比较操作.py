# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.07
"""

# 比较规则:依次比较
# 比较原理:比较原始值,调用内置函数ord可以得到指定字符的原始值,与内置函数ord相对应的是内置函数chr

print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord('b'))
print(chr(97), chr(98))
print(ord('杨'))
print(chr(26472))

# == 与 is的区别
# ==比较的valie
# is 比较的是id

a = b = 'Python'
c = 'Pytohn'
print(a == b)
print(b == c)

print(a is b)
print(b is c)
print(id(a))
print(id(b))
print(id(c))