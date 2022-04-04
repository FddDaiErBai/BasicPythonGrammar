# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

for item in 'Python':
    print(item)


# range()产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循坏体中不需要使用到自定义变量,可将自定义变量写为"_"
for _ in range(5):
    print('人生苦短,我用python')

# 计算1到100之间的偶数和
sum = 0
for item in range(1, 101):
    if item % 2 == 0:
        sum += item
print('1到100之间的偶数和为:', sum)
