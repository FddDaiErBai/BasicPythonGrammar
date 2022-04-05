# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.05
"""

# 向列表的末尾添加一个元素
lst = ['Hello', 10, 'world']
print('添加之前:', lst, id(lst))

lst.append(100)
print('添加之后:', lst, id(lst))

lst2 = ['Allen', 'Mary']
lst.append(lst2)  # 将lst2作为一个元素添加到lst末尾
print(lst)

lst.extend(lst2)  # 向lst末尾一次性添加多个元素
print(lst)

# 在任意位置上添加元素
lst.insert(1, 90)
print(lst)

# 在任意的位置上添加N多个元素,切掉!
lst3 = [50, 60, 70]
lst[1:] = lst3
print(lst)