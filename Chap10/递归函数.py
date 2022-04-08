# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""


def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)


print(fac(6))
