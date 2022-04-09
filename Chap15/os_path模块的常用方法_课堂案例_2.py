# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

import os

# path=os.getcwd()
path = '/Users/leomashiro/MaShiBinEdu/BasicPythonGrammar/'
lst_files = os.walk(path)  # walk可以遍历指定路径下的所有文件以及目录
print(lst_files)
for dirpath, dirname, filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('-------------------------------')'''

    for dir in dirname:
        print(os.path.join(dirpath, dir))
    for file in filename:
        print(os.path.join(dirpath, file))