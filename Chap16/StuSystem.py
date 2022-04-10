# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""
file_name='student.txt'

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
        stu_txt=open(file_name,'a',encoding='utf-8')      
    except:
        stu_txt=open(file_name,'w',encoding='utf-8')
        
    for item in lst:
        stu_txt.write(str(item)+'\n')
    
    stu_txt.close()
    

def insert():
    student_list=[]
    while True:
        id=input('请输入学生的id(如1001):')
        if not id:
            break
        name=input('请输入姓名:')
        if not name:
            break
        try:
            en_list=int(input('请输入英语成绩:'))
            python_list=int(input('请输入python成绩:'))
            java_list=int(input('请输入java成绩:'))
            
        except:
            print('输入无效,不是整数类型,请重新输入')
            continue
        
        # 将录入的学生信息保存到字典中
        student={'id':id,'name':name,'en_list':en_list,'python_list':python_list,'java_list':java_list}
        student_list.append(student)
        answer=input('是否继续添加?')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    
    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕!')

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