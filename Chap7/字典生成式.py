# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.06
"""

items = ['Fruits', 'Books', 'Others', ]
prices = [96, 78, 85, 33, 55]

d = {item: price for item, price in zip(items, prices)}  # 以元素少的为基准
print(d)