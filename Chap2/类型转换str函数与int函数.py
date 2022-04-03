# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.02
"""

name = '张三'
age = 20

print(type(name), type(age))
print('我叫'+name+'今年，'+str(age)+'岁')

print('----------------str()函数将其他类型转成str类型------')

a = 10
b = 12.32
c = False

print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))

print('-----------------int()将其他类型转成int类型-----')

s1 = '128'
f1 = 92.2
s2 = '76.77'
f2 = True
s3 = 'Hello'

print(type(s1), type(f1), type(s2), type(f2), type(s3))
print(int(s1), type(int(s1)))  # 将str类型转成int类型，字符串为数字串
print(int(f1), type(int(f1)))  # 将float类型转成int类型，截取整数部分，舍掉小数部分
# print(int(s2),type(int(s2))) #将str转成int类型，报错，因为字符串为小数串
print(int(f2), type(int(f2)))
# print(int(s3),type(int(s3))) #将str类型转成int类型时，字符串必须为数字串（整数），非数字串不允许转换
