# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.04
"""

for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()