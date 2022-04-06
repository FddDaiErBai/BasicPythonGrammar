# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

s = 'Hello,Hello'
# 正向查找第一个
print(s.index('lo'))  # 3 若不存在,ValueError:substring not found
print(s.find('lo'))  # 3 若不存在,返回-1

# 逆向查找第一个
print(s.rindex('lo'))  # 9 若不存在,ValueError:substring not found
print(s.rfind('lo'))  # 9 若不存在,返回-1