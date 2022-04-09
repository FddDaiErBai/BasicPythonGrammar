# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

print(type(open('a.txt', 'a')))
with open('a.txt', 'r') as file:
    print(file.read())


'''
MyContentMgr实现了特殊方法__enter()___,__exit()__称为改类对象遵守了上下文管理器协议
该类对象的实例对象,称为上下文管理器
'''


class MyContentMgr(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self

    def show(self):
        pass


with MyContentMgr() as file:  # 相当于file=MyContentMgr()
    file.show()


# 文件的复制
with open('a.txt', 'r') as src_file:
    with open('a_copy', 'w') as target_file:
        target_file.write(src_file.read())