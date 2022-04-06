# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

import sys

# 字符串是Python中的基本数据类型,是一个不可变的字符序列

# 字符串的定义
a = 'Python'
b = "Python"
c = '''Python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 驻留机制的几种情况(交互模式)
# 字符串的长度为0或1时
# 符合标识符的字符
# 字符串只在编译时驻留,而非运行时
# [-5,256]之间的整数数字

# sys中的intern方法强制2个 、字符串指向同一个对象
# Pycharm对字符进行了优化处理

a = 'abc'
b = 'a'+'bc'  # 运行前已经连接完毕
c = ''.join(['a', 'bc'])  # 在运行时,通过join方法对列表中的数据进行连接
print(a is b)
print(a is c)

a = 'abc%'
b = 'abc%'
a = sys.intern(b)
print(a is b)

# 字符串驻留机制的优缺点
"""
当需要值相同的字符串时,可以直接从字符串池里拿来使用,避免频繁地创建和销毁,提升效率和节约内存,
因此拼接字符串和修改字符串是会比较影响性能的

在需要进行字符串拼接时建议使用str类型的join方法,而非+,因为join()方法是先计算出所有字符中
的长度,然后再拷贝,只new一次对象,效率要比"+"效率高
"""