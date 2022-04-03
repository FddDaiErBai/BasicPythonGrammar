# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

"""
会员
>=200 8折
>=100 9折
不打折

非会员
>200 9.5折
不打折
"""

answer = input('您是会员吗?y/n\n')
money = float(input('请输入您的购物金额:\n'))
# 判断会员
if answer == 'y':
    if money >= 200:
        print('打8折,付款金额为:', money*0.8)
    elif money >= 100:
        print('打9,付款金额为:', money*0.9)
    else:
        print('不打折，付款金额为:', money)
else:
    if money >= 200:
        print('打9.5折,付款金额为:', money*0.95)
    else:
        print('不打折，付款金额为:', money)
