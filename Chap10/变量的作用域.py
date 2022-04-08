# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def func(a, b):
    c = a+b  # c称为局部变量,因为c是在函数体内进行定义的变量,a,b为函数的形参,作用范围也是函数内部,相当于局部变量
    print(c)


# print(c)
# print(a) a,c超出作用域

name = '杨老师'  # name的作用范围为函数内部和外部都可以使用,称为全局变量
print(name)


def func2():
    print(name)


func2()


def func3():
    global age  # 函数内部定义的变量,局部变量,局部变量使用global声明,这个变量是实际上就变成全局变量
    age = 20
    print(name)


func3()
print(age)