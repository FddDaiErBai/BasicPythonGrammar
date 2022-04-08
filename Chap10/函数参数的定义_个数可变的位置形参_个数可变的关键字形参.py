# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def func(*args):  # 函数定义时,可变的位置参数
    print(args)
    print(args[0])


func(10)
# 结果为元组
func(12, 70)
func(45, 34, 60)


def func1(**args):
    print(args)


func1(a=10)
func1(a=20, b=30, c=40)  # 结果为字典

# def func2(*args,*a): 报错,个数可变的位置参数只能是1个

# def func2(**args,**args): 报错,个数可变的关键字参数只能是1个


def func2(*args1, **args2):
    pass


# def func3(**args1,*args2): 报错

'''
在一个函数定义过程中,既有个数可变的关键字参数,也有个数可变的位置形参,
要求,个数可变的位置形参,放在个数可变的关键字形参之前
'''