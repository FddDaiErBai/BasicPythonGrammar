# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.05
"""

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
lst.remove(30)  # 从列表中移除一个元素,若存在重复元素只移除第一个
print(lst)

# lst.remove(100) 若不存在,ValueError

# 根据索引移除元素
lst.pop(1)
print(lst)
# lst.pop(5) 若不存在,ValueError
lst.pop()  # 若不指定参数，=,默认删除最后一个元素
print(lst)

# 切片操作,删除至少一个元素,将产生一个新的列表元素
new_lst = lst[1:3]
print('原列表:', lst)
print('切片后原列表:', new_lst)

# 不产生新的列表对象,而是删除原列表中的内容
lst[1:3] = []
print(lst)

# 清除列表中的所有元素
lst.clear()
print(lst)

# 使用del语句删除列表对象
del lst
# print(lst) NameError:name 'lst' is not defined