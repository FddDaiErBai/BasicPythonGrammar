# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

# 面向对象的三大特征:封装,继承,多态


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动')


car = Car('宝马')
car.start()
print(car.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# 在类的外部使用name与age
print(stu.name)
# print(stu.__age) # 不允许访问

# print(dir(stu))

print(stu._Student__age)  # 在类的外部可以通过_Student__age进行访问,不建议访问