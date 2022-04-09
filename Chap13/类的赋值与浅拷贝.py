# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

import copy


class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值
cpu1 = Cpu()
cpu2 = cpu1
print(cpu1)
print(cpu2)

# 类的浅拷贝
disk = Disk()
computer = Computer(cpu1, disk)


computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer.disk)