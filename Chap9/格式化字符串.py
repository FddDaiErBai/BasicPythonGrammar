# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""

# %作占位符 %s字符串 %i或%d整数 %f浮点数

name = '张三'
age = 20
print('我叫%s,今年%d岁' % (name, age))

# {}作占位符
print('我叫{0},今年{1}岁'.format(name, age))

# f-string
print(f'我叫{name},今年{age}岁')

# 精度和宽度
print('%d' % 99)
print('%10d' % 99)  # 宽度
print('%f' % 3.1415926)
print('%.3f' % 3.1415926)  # 精度
print('%10.3f' % 3.1415926)  # 同时表示

print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))  # 0.3表示一共是3位数
print('{0:.3f}'.format(3.1415926))  # 0.3f表示
print('{0:10.3f}'.format(3.1415926))