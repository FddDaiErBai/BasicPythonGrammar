# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""

# 编码
s = '天涯共此时'
print(s.encode(encoding='GBK'))  # 在GBK这种编码格式中一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编码格式中一个中文占三个字节

# 解码
# byte代表就是一个二进制数据(字节类型的数据)
byte = s.encode(encoding='GBK')  # 编码
print(byte.decode(encoding='GBK'))  # 解码

byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))