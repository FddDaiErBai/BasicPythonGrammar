# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.23
"""

# 1.使用print的方式进行输出(输出的目的地是文件)

fp = open(
    '/Users/leomashiro/MaShiBinEdu/BasicPythonGrammar/Chap17/实例案例一/text.txt', 'w')
print('奋斗成就更好的你!', file=fp)
fp.close()

# 2.使用文件的读写操作

with open('/Users/leomashiro/MaShiBinEdu/BasicPythonGrammar/Chap17/实例案例一/text2.txt', 'w') as file:
    file.write('奋斗成就更好的你!')