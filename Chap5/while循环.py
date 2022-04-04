# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

a = 1
# 判断套件表达式
while a < 10:
    # 执行条件执行体
    print(a)
    a += 1
# while 判断N+1次，条件为True执行N次

# 计算0到4之间的累加和
# 1. 初始化变量
# 2. 条件判断
# 3. 条件执行体(循环体)
# 4. 改变变量

a = 0
sum = 0
while a < 5:
    sum += a
    a += 1
print('和为:', sum)
