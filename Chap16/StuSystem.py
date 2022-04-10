# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""
import os


file_name = 'student.txt'


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


def save(lst):
    try:
        stu_txt = open(file_name, 'a', encoding='utf-8')
    except:
        stu_txt = open(file_name, 'w', encoding='utf-8')

    for item in lst:
        stu_txt.write(str(item)+'\n')

    stu_txt.close()


def insert():
    student_list = []
    while True:
        id = input('请输入学生的id(如1001):')
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            en_list = int(input('请输入英语成绩:'))
            python_list = int(input('请输入python成绩:'))
            java_list = int(input('请输入java成绩:'))

        except:
            print('输入无效,不是整数类型,请重新输入')
            continue

        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'en_list': en_list,
                   'python_list': python_list, 'java_list': java_list}
        student_list.append(student)
        answer = input('是否继续添加?')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕!')


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息,无数据信息!')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))

    # 定义内容的显示格式

    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    for item in lst:
        print(format_data.format(item.get('id'), item.get('name'), item.get('en_list'), item.get(
            'python_list'), item.get('java_list'), int(item.get('en_list'))+int(item.get('python_list'))+int(item.get('java_list'))))


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(file_name):
            mode = int(input('按id查找请输入1,按姓名查找请输入2:'))
            if mode == 1:
                id = input('请输入学生的id:')
            elif mode == 2:
                name = input('请输入学生姓名:')
            else:
                print('您的输入有误,请重新输入!')
                search()
            with open(file_name, 'r', encoding='utf') as r_file:
                student = r_file.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)

            # 清空列表
            student_query.clear()
            answer = input('是否要继续查询?')
            if answer == 'y' or answer == 'Y':
                continue

            else:
                break

        else:
            print('暂未保存学生信息')
            return


def delete():
    while True:
        student_id = input('请输入要删除学生到id:')
        if student_id != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []

            flag = False  # 标记是否删除

            if student_old:
                with open(file_name, 'w', encoding='utf-8') as file:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            file.write(str(d)+'\n')
                        else:
                            flag = True

                        if flag:
                            print('id为{student_id的学生信息已被删除}')
                        else:
                            print('没有找到id为{student_id}的学生信息')

            else:
                print('无学生信息')
                break

            show()  # 删除之后要重新显示所以学生信息
            answer = input('是否要继续删除?')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as r_file:
            student_old = r_file.readlines()
    else:
        return

    student_id = input('请输入要修改学生的id:')
    if student_id:
        with open(file_name, 'w', encoding='utf-8') as w_file:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == student_id:
                    print('找到学生信息,可以修改学生信息!')
                    while True:
                        try:
                            d['name'] = input('请输入姓名:')
                            d['en_list'] = input('请输入英语成绩:')
                            d['python_list'] = input('请输入python成绩:')
                            d['java_list'] = input('请输入java成绩:')
                        except:
                            print('您的输入有问题,请重新输入!')
                        else:
                            break
                    w_file.write(str(d)+'\n')
                    print('修改成功!')
                else:
                    w_file.write(str(d)+'\n')
            answer = input('是否继续修改其他学生信息')
            if answer == 'y' or answer == 'Y':
                modify()
    else:
        return


def sort():
    pass


def total():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as r_file:
            students = r_file.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')

    else:
        print('暂未保存数据信息!')


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