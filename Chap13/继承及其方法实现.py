# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self, name, age, teach_of_year):
        super.__init__(name, age)
        self.teach_of_year = teach_of_year


stu = Student('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)

stu.info()
teacher.info()

# 多继承


class A(object):
    pass


class B(object):
    pass


class C(A, B):
    pass