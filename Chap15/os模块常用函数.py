# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

# os模块是与操作系统相关的一个模块
import os

# os.system('python3') # 执行终端

# os.system('open -a QQ')

# os.startfile('path') Win

print(os.getcwd())  # 返回当前工作目录
# 返回指定路径下的文件和目录信息
lst = os.listdir('/Users/leomashiro/MaShiBinEdu/BasicPythonGrammar/Chap15')
print(lst)

# 创建目录
# os.mkdir('new_dir')

# 创建多级目录
# os.mkdirs('A/B/C')

# 删除目录
# os.rmdir('new_dir')

# 删除多级目录
# os.rmdirs('A/B/C')

# 将path设置为当前的工作目录
# os.chdir(path)