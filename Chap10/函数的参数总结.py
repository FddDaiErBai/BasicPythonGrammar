import py_compile


# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def func(a, b, c):  # a,c,b为形参
    print(a)
    print(b)
    print(c)


# 函数的调用
func(10, 20, 30)  # 函数调用时的参数传递,称为位置传参
lst = [11, 22, 33]
func(*lst)  # 在函数调用时,将列表中的每个元素都转换为位置实参传入

func(a=100, b=200, c=300)  # 函数的调用,关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
func(**dic)  # 在函数调用时,将字典中的键值对都转换为实参


def func1(a, b=10):  # b时在函数的定义处,所以b是实参,而且进行了赋值,所以b为默认值参数
    print(a)
    print(b)


def func2(*arg):  # 个数可变的位置形参
    pass


def func3(**arg):  # 个数可变的关键字形参
    pass


func2(10, 20, 30, 40)
func3(a=11, b=22, c=33, d=44, e=55)


def func4(a, b, *, c, d):  # 从*之后的参数,在函数调用时,只能采用关键字实参传递
    print(a)
    print(b)
    print(c)
    print(d)


# func4(10,20,30,40) # 位置实参传递
func4(a=11, b=22, c=33, d=44)  # 关键字实参传递
func4(10, 20, c=30, d=40)

# c,d只能采用关键字实参传递

# 函数定义时的形参的顺序问题


def func5(a, b, *, c, d, **args):
    pass


def func6(*args, **args2):
    pass


def func7(a, b=10, *args, **args2):
    pass