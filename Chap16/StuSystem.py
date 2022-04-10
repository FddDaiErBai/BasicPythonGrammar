# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""


def menu():
    print('=================================学生管理系统=================================')
    print('-----------------------------------功能菜单-----------------------------------')
    print('\t\t\t\t1.录入学生系统')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所以学生信息')
    print('\t\t\t\t0.退出')
    print('----------------------------------------------------------------------------')


def insert():
    pass


def search():
    pass


def delete():
    pass


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


def main():
    while True:
        menu()
        choice = int(input('请选择:'))
        if choice in list(range(8)):
            if choice == 0:
                answer = input('您确定要退出系统吗?')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用!')
                    break  # 退出系统
                else:
                    continue

            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort()  # 排序
            elif choice == 6:
                total()  # 统计总人数
            elif choice == 7:
                show()  # 显示学生信息


if __name__ == '__main__':
    main()