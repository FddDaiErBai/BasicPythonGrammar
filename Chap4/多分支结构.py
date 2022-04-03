# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

# 多分支结构
# 录入整数成绩，判断范围
score = int(input('请输入一个成绩:'))
# 判断
if score <= 0 or score >= 100:
    print('对不起，成绩有误，不在有效范围内！')
elif score >= 90 and score < 100:
    print("A")
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D')
elif score >= 0 and score <= 59:
    print('E')

# python中可写:90<=score<=100
