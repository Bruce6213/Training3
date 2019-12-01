# Author  : Bruce li
# Date    : From 2019/11/22 to 2019/11/30
# Describe: 学员类
# Trouble : None


import class_manager, class_school
# 学员类
class Student(object):
    def __init__(self, name, age, sex, school, s_class):
        """个人信息"""
        self.name = name
        self.age = age
        self.sex = sex
        self.school = school
        self.s_class = s_class
        self.score = -1
    def view_information(self):
        """查看个人及班级信息"""
        print('info about %s'.center(60, '*')%self.name)
        print('Name: ', self.name, '\n', 'Age: ', self.age, '\n', 'Sex: ', self.sex)
        print('university: ', self.school, '\n', 'Class: %s 班'%self.s_class.course)
    @staticmethod
    def register():
        """注册"""
        #while True:
        name = input('请输入您的姓名: ')
        age = input('请输入您的年龄: ')
        sex = input('请输入您的性别: ')
        print('查看学校信息'.center(60, '*'))
        for i in class_manager.Manager.schools:
            print('%d、%s university'%(class_manager.Manager.schools.index(i) + 1, i.name))
        while True:
            choice = input('==>')
            if choice.isdigit():
                if int(choice) in range(1, len(class_manager.Manager.schools) + 1):
                    class_manager.Manager.schools[int(choice) - 1].view_info()
                    reply = int(input('您的心仪学校是(序号): '))
                    reply2 = int(input('您的心仪班级是(序号): '))
                    if class_manager.Manager.schools[reply - 1].school_class[reply2 - 1].current_num == \
                            class_manager.Manager.schools[reply - 1].school_class[reply2 - 1].limit:
                        print('%s 班人数已满'%class_manager.Manager.schools[reply - 1].school_class[reply2 - 1].course)
                        print("\033[1;32;44m别灰心，听说隔壁班也是比较不错的哦！\033[0m".center(60))
                    else:
                        new_student = Student(name, age, sex, class_manager.Manager.schools[reply - 1].name,
                                class_manager.Manager.schools[reply - 1].school_class[reply2 - 1])
                        print("\033[1;30;41m注册成功！\033[0m".center(60))
                        class_manager.Manager.schools[reply - 1].school_class[reply2 - 1].current_num += 1
                        print('亲爱的%s同学:'%new_student.name)
                        print('您的登入账号为: ', new_student.name)
                        passwd = class_manager.Random()
                        new_student.account = new_student.name
                        new_student.passwd = passwd
                        print('您的登入密码为: %d\n\033[0;30;41m建议你立即修改密码以避免账号被他人非法登入。\033[0m' % passwd)
                        class_manager.student_account[new_student.name] = passwd
                        class_school.Class.students.append(new_student)
                        class_manager.Manager.schools[reply - 1].school_class[reply2 - 1].per_students.append(new_student)
                        reply = input('==>(y/n) ')
                        if reply.lower() == 'y':
                            class_manager.change(0, new_student)
                    break
                else:
                    print("404 Not Found")
                    continue
            elif choice == 'b' or choice == 'q':
                break
            else:
                print('\033[0;31;40mWhat!!!\033[0m')
                continue
    def mark(self):
        if self.score == -1:
            print("\033[1;30;45m睡蒙了吧， 明天才开始考试！\033[0m".center(60))
        else:
            print('your score is ', self.score)
def student_main():
    while True:
        user = input('请输入登入账号: ')
        passwd = int(input('请输入登入密码(数字): '))
        if class_manager.student_account.get(user) and class_manager.student_account[user] == passwd:
            print('欢迎登入'.center(60, '*'))
            break
        print("\033[1;30;41m用户名或者密码错误！\033[0m".center(60))
    return (user, passwd)
if __name__ == "__main__":
    pass