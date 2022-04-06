# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

s = 'Hello world python'
lst = s.split()  # 默认分隔符为空格,返回一个列表
print(lst)

s1 = 'Hello|world|Python'
print(s1.split(sep='|'))  # 指定分割符为'|'
print(s1.split(sep='|', maxsplit=1))  # 指定最大分割次数,剩余右边成一个部分

# rsplit()从右侧开始分割
print(s1.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))  # 指定最大分割次数,剩余左边成一个部分