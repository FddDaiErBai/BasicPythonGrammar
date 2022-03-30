"""
author: FddDaiErBai
date: 2022.03.30
"""
# 输出数字
print(520)
print(3.12)

# 输出字符串
print('Hello world!')
print("Hello world!")

# 输出含有运算符的表达式
print(3 + 1)

# 输出文件
fp = open('G:/MaShiBinEdu/文件输出/print输出/text.txt', 'a+')
print("Hello world!", file=fp)
fp.close()

# 不进行换行输出
print('Hello', 'world', 'Leo')
