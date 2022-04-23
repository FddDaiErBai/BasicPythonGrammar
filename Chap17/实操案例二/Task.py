# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.23
"""

import random

price=random.randint(1000,1500)
print('今日竞猜的商品为小米扫地机器人:价格在1000-1500之间')
guess=int(input())
if guess>price:
    print('大了')
elif guess<price:
    print('小了')
else:
    print('猜对了')
    
print(price)
    