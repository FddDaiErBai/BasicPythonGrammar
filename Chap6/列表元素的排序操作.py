# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.05
"""

lst = [11, 47, 33, 34, 52, 84, 65, 56, 79]
print('排序前', lst, id(lst))

# 开始排序,调用列表对象的sort方法,默认升序排序
lst.sort()
print('排序后', lst, id(lst))

# 通过指定参数,将列表元素进行降序
lst.sort(reverse=True)  # reverse=True降序,reverse=False升序
print(lst)

# 调用内置函数sorted()排序,将产生一个新的列表对象
print('排序前', lst)

# 开始排序
new_lst = sorted(lst)
print(lst)
print(new_lst)

# 指定参数，实现降序
desc_lst = sorted(lst, reverse=True)
print(desc_lst)