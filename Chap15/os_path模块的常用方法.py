# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

import os.path

print(os.path.abspath('a.txt'))  # 获取文件或目录的绝对路径

print(os.path.exists('a.txt'), os.path.exists('b.txt'))  # 判断文件是否存在

# (os.path.join(path,path)) # 将目录与目录或者文件名拼接起来
# (os.path.split(path,path)) # 将目录与目录或者文件名分离
print(os.path.splitext('a.txt'))  # 分离文件和扩展名
print(os.path.basename(
    '/Users/leomashiro/MaShiBinEdu/BasicPythonGrammar/Chap15/a.txt'))  # 从一个目录中提取文件名
# 从一个路径中提取文件路径,不包括文件名
print(os.path.dirname('/Users/leomashiro/MaShiBinEdu/BasicPythonGrammar/Chap15/a.txt'))
print(os.path.isdir(
    '/Users/leomashiro/MaShiBinEdu/BasicPythonGrammar/Chap15/a.txt'))  # 判断是否为路径