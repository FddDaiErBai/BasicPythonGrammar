# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

money = 1000  # 余额
s = int(input('请输入取款金额:\n'))  # 取款金额
# 判断余额是否充足
if money >= s:
    money -= s
    print('取款成功，余额为:', money)
