# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""
'''
file = open('a.txt', 'r')
print(file.read(2))
print(file.readline())
print(file.readlines())
file.close()
'''

'''
file = open('a.txt', 'w')
file.write('Hello,world')
lst=['java','python']
file.writelines(lst)
file.close()
'''

'''
file = open('a.txt', 'r')
file.seek(2) 移动文件指针位置 一个中文两个字节
print(file.read())
print(file.tell()) 返回当前文件指针位置
file.close()
'''

'''
file = open('a.txt', 'a')
file.write('Hello')
file.flush()
file.wirte('world')
file.close()
'''