# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

# 录入两个整数，比较大小

a = int(input('请输入一个整数'))
b = int(input('请输入另一个整数'))

"""if a>=b:
    print(a,'>=',b)
else:
    print(a,'<',b)
"""

print(str(a)+'>='+str(b) if a >= b else str(a)+'<'+str(b))
