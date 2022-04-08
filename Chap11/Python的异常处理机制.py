# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.08
"""

# try-except

try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a/b

except ZeroDivisionError:
    print('除数不允许为0')

except ValueError:
    print('只能输入数字串')

# except BaseException:

else:
    print(result)


finally:
    print('无论程序是否出错,都会被执行')