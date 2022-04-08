# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def func(arg1, arg2):
    print(arg1)
    print(arg2)
    arg1 = 100
    arg2.append(10)
    print(arg1)
    print(arg2)
    # return


n1 = 11
n2 = [22, 33, 44]
print(n1)
print(n2)
func(n1, n2)  # 位置传参,arg1,arg2是函数定义处的形参,n1,n2是函数调用处的实参,总结,实参名称与形参名称可以不一致

print(n1)
print(n2)

'''
在函数调用的过程中,进行参数的传递
如果是不可变对象,在函数体内的修改不会影响实参的值
如果是可变对象,在函数体内的修改会影响到实参的值
'''