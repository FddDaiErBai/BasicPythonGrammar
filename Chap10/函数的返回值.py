# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def func(num):
    odd = []
    even = []
    for i in num:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


lst = [10, 29, 34, 23, 44, 53, 55]
print(func(lst))

'''
函数的返回值
如果函数没有返回值,函数执行完毕后,不需要给调用处提供数据
函数的返回值,如果是1个,直接返回原值
函数的返回值,如果是多个,返回的结果为元组
'''


def fuc():
    print('Hello')
    # return


def func2():
    return 'Hello'


res = func2()
print(res)


def func3():
    return 'Hello', 'world'


print(func3())

# 函数在定义时,是否需要返回值,视情况而定