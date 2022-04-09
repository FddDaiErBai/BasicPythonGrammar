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


cpu1 = Cpu()
cpu2 = cpu1
print(cpu1)
print(cpu2)

disk = Disk()
computer = Computer(cpu1, disk)

# 深拷贝
computer2 = copy.deepcopy(computer)

print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer.disk)