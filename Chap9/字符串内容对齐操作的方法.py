# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

s = 'Hello,world'

# 居中对齐
print(s.center(20, '*'))  # 宽度小于原字符串长度,返回原字符串

# 左对齐
print(s.ljust(20, '*'))
print(s.ljust(10))  # 宽度小于原字符串长度,返回原字符串
print(s.ljust(20))  # 默认填充符为空格

# 右对齐
print(s.rjust(20, '*'))
print(s.rjust(10))  # 宽度小于原字符串长度,返回原字符串
print(s.rjust(20))  # 默认填充符为空格

# 右对齐,使用0进行填充
print(s.zfill(20))
print(s.zfill(10))  # 宽度小于原字符串长度,返回原字符串
print('-8910'.zfill(8))  # 在减好后添加0