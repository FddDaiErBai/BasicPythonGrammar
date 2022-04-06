# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

s = 'Hello,python'
# 判断指定字符串是否为合法标识符
print(s.isidentifier())
print('Hello'.isidentifier())
print('张三_'.isidentifier())
print('张三_123'.isidentifier())

# 判断指定字符串是否全部由空白字符组成
print('\t'.isspace())

# 判断指定字符串是否全部由字母组成
print('abc'.isalpha())
print('张三'.isalpha())
print('张三1'.isalpha())

# 判断指定字符串是否全部由十进制数字组成
print('123'.isdecimal())
print('1234四'.isdecimal())

# 判断指定字符串是否全部由数字组成
print('123'.isnumeric())
print('123四'.isnumeric())
print('ⅡⅡⅡ'.isnumeric())

# 判断指定字符串是否全部由字母,数字组成
print('adc1'.isalnum())
print('张三123'.isalnum())
print('abc!'.isalnum())