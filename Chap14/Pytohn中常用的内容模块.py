# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

import sys  # 与Python解释器及其环境操作相关的标准库
import time  # 提供与时间相关的各种函数的标准库
import os  # 提供访问操作系统服务功能的标准库
import calendar  # 提供与日期相关的各种函数的标准库
import urllib.request  # 用于读取来自网上(服务器)的数据标准库
import json  # 用于使用json序列化和反序列化对象
import re  # 用于在字符串中执行正则表达式匹配和替换
import math  # 提供标准算术运算函数的标准库
import decimal  # 用于进行精确控制运算精度,有效数位和四舍五入操作的十进制运算
import logging  # 提供灵活的记录事件,错误,警告和调试信息等日志信息的功能

print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())

print(math.pi)