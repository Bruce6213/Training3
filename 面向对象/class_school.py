# Author  : Bruce li
# Date    : From 2019/11/22 to 2019/11/30
# Describe: 学校类
# Trouble : None


import class_teacher, class_manager
# 课程类
class Course(object):
    def __init__(self):
        pass
# 班级类
class Class(object):
    students = []
    def __init__(self, expenses, time, limit, course, current_num = 0):
        self.expenses = expenses
        self.time = time
        self.limit = limit
        self.course = course
        self.current_num = current_num
        self.per_students = []
    def introduction(self):
        print('info about the %s class'.center(60, '*')%self.course)
        print('本班学习内容: %s' % self.course)
        print('本班学习时长: %d个月'%self.time)
        print('本班学费：%dRMB'%self.expenses)
        print('本班当前报名人数: %d'%self.current_num)
        print('本班人数上限为: %d'%self.limit)
# 学校类
class School(object):
    def __init__(self, name, addr):
        """学校信息"""
        self.teachers = []
        self.school_class = []
        self.name = name
        self.addr = addr
    def employ(self, t_class, t_course):
        """聘请教师"""
        t_name = input('请输入本班上课教师的姓名: ')
        t_age = input('请输入本班上课教师的年龄: ')
        t_sex = input('请输入本班上课教师的性别: ')
        teacher = class_teacher.Teacher(t_name, t_age, t_sex, t_course, self.name, t_class)
        self.teachers.append(teacher)
        print('='.center(60, '='))
        print('尊敬的%s老师：'%teacher.name)
        print('您的登入账号为: ', teacher.name)
        passwd = class_manager.Random()
        print('您的登入密码为: %d\n建议你立即修改密码以避免账号被他人非法登入。'%passwd)
        teacher.account = teacher.name
        teacher.passwd = passwd
        class_manager.teacher_account[teacher.name] = passwd
        print('='.center(60, '='))
        reply = input('==>(y/n) ')
        if reply.lower() == 'y':
            class_manager.change(1, teacher)
    def creat_class(self, num):
        """创建班级"""
        c_expenses = float(input('请输入第%d个班的学费: ' % (num + 1)))
        c_time = int(input('请输入第%d个班的学习时长(月): ' % (num + 1)))
        c_limit = int(input('请输入第%d个班的最大招生数: ' % (num + 1)))
        c_course = input('请输入第%d个班的课程: ' % (num + 1))
        new_class = Class(c_expenses, c_time, c_limit, c_course)
        self.school_class.append(new_class)
        return new_class
    def creat_course(self):
        """创建课程"""
        pass
    def view_info(self):
        print('info about %s school'.center(60, '*')%self.name)
        while True:
            print('1、师资力量')
            print('2、班级情况')
            choice = input('==>')
            if choice == '1':
                while True:
                    print('%s university 共有%d名教师, 他们分别是:'%(self.name, len(self.teachers)))
                    for i in self.teachers:
                        print(self.teachers.index(i) + 1, '、', i.name)
                    # 查看老师信息
                    choice = input('==>')
                    if choice.isdigit():
                        if int(choice) in range(1, len(self.teachers) + 1):
                            self.teachers[int(choice) - 1].view_info()
                            class_manager.tips()
                        else:
                            print('\033[0;31;40mWhat!!!\033[0m')
                            continue
                    else:
                        if choice == 'b' or choice == 'q':
                            break
                        else:
                            print('\033[0;31;40mWhat!!!\033[0m')
                            continue
            elif choice == '2':
                while True:
                    print('%s university 共有%d个班，分别为:'%(self.name, len(self.school_class)))
                    for i in self.school_class:
                        print('%d班: %s班'%(self.school_class.index(i) + 1, i.course))
                    # 查看班级信息
                    choice = input('==>(序号)')
                    if choice.isdigit():
                        self.school_class[int(choice) - 1].introduction()
                        class_manager.tips()
                    elif choice == 'b' or choice == 'q':
                        break
                    else:
                        print('\033[0;31;40mWhat!!!\033[0m')
                        continue
            # 按'q'就退出
            elif choice.lower() == 'q' or choice.lower() == 'b':
                break
            else:
                print('404 NotFound...')
                continue
if __name__ == "__main__":
    pass

