# Author  : Bruce li
# Date    : From 2019/11/22 to 2019/11/30
# Describe: 讲师类
# Trouble : None


import class_manager, random, time
# 讲师类
class Teacher(object):
    def __init__(self, name, age, sex, major, school_name, t_class):
        self.name = name
        self.age = age
        self.sex = sex
        self.major = major
        self.school_name = school_name
        self.t_class = t_class
    def view_info(self):
        """查看个人及班级信息"""
        print('info about %s teacher'.center(60, '*') % self.name)
        print('性别: ', self.sex)
        print('年龄: ', self.age)
        print('主修: ', self.major)
        print('工作单位: %s university' % self.school_name)
        print('上课班级: %s班' % self.t_class.course)
    def score(self):
        """学生成绩"""
        if not self.t_class.per_students:
            print("\033[1;30;42m明天才开始考试！\033[0m".center(60))
        else:
            for i in range(self.t_class.current_num):
                print('%s 的成绩为：%d'%(self.t_class.per_students[i].name, self.t_class.per_students[i].score))
    def examination(self):
        if not self.t_class.current_num:
            print("\033[1;31;42m课程质量太low, 目前为止没有一个学生报名！\033[0m".center(60))
        else:
            print('\n考试进行中'.center(60, '*'))
            for i in range(self.t_class.current_num):
                self.t_class.per_students[i].score = random.randint(30, 100)
            time.sleep(5)
            print('\n考试结束'.center(60, '*'))
def teacher_main():
    while True:
        user = input('请输入登入账号: ')
        passwd = int(input('请输入登入密码(数字): '))
        if class_manager.teacher_account.get(user) and class_manager.teacher_account[user] == passwd:
            print("\033[1;32;41m欢迎登入！\033[0m".center(60))
            break
        print("\033[1;30;41m用户名或者密码错误！\033[0m".center(60))
    return (user, passwd)
if __name__ == "__main__":
    pass
