# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


print(Fibonacci(6))

for i in range(1, 7):
    print(Fibonacci(i))