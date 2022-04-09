# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""


class Animal(object):
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat():
        print('人吃五谷杂粮')


def func(obj):
    obj.eat()


func(Cat())
func(Dog())
func(Animal())