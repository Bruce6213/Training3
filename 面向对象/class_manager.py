# Author  : Bruce li
# Date    : From 2019/11/22 to 2019/11/30
# Describe: 管理员类
# Trouble : None


import class_school, random

# 学生账号
student_account = {}
# 讲师账号
teacher_account = {}
def change(flag, obj):
    """修改密码"""
    while True:
        passwd = int(input('请输入新密码(数字)：'))
        temp = int(input('请再次输入新密码(数字)：'))
        if passwd == temp:
            if flag == 0:
                student_account[obj.account] = passwd
                obj.passwd = passwd
            else:
                teacher_account[obj.account] = passwd
                obj.passwd = passwd
            print("\033[0;30;46m密码修改成功！\033[0m".center(60))
            print('\n\n\n')
            break
        else:
            print("\033[1;31;40m两次输入的新密码不一致！\033[0m".center(60))
            continue
def match(flag, user, passwd):
    '根据用户名和密码来匹配对象并将其返回'
    if flag == 0:
        for i in Manager.schools:
            for j in i.teachers:
                if user == j.account and passwd == j.passwd:
                    return j
    else:
        for i in Manager.schools:
            for j in i.school_class:
                for k in j.students:
                    if k.account == user and k.passwd == passwd:
                        return k
def tips():
    '提示信息'
    while True:
        reply = input("==>\033[1;30;42m(友情提示：按b或q返回上一层)\033[0m")
        if reply.lower() == 'b' or reply.lower() == 'q':
            break
        else:
            print('\033[0;31;40mWhat!!!\033[0m')
            continue
def Random():
    """产出随机数"""
    return random.randint(100000, 999999)
class Manager(object):
    # 子类继承父类, 默认无法使用父类的私有方法和私有属性
    schools = []
    # 实例对象无法更改类属性, 如果强写对象.类属性 = xxx
    # 只是给这个对象添加了一个实例变量, 而实例变量的名字恰好等于类属性罢了
    # 类属性的值是不会变的
    def view_info(self):
        """查看学校信息"""
        while True:
            for i in self.schools:
                print('%d、%s university'%(self.schools.index(i) + 1, i.name))
            reply = input('==>')
            if reply.isdigit():
                if int(reply) in range(1, len(self.schools) + 1):
                    self.schools[int(reply) - 1].view_info()
                else:
                    print('\033[0;31;40mWhat!!!\033[0m')
                    continue
            elif reply == 'b' or reply == 'q':
                break
            else:
                print('\033[0;31;40mWhat!!!\033[0m')
                continue
    def Creat(self):
        """创建学校"""
        s_name = input('请输入新学校的名称:')
        s_addr = input('请输入新学校的地址:')
        new_school = class_school.School(s_name, s_addr)
        Manager.schools.append(new_school)
        num = int(input('准备开设多少个班级:'))
        for i in range(num):
            new_class = new_school.creat_class(i)
            new_school.employ(new_class, new_class.course)
        print("\033[1;30;42m今日起正式投入使用！\033[0m".center(60))

def manager_main():
    while True:
        print('1、查看学校信息')
        print('2、创建新的学校')
        reply = input('==>')
        if reply.isdigit():
            man = Manager()
            if reply == '1':
                if Manager.schools:
                    man.view_info()
                else:
                    print("\033[1;30;42m方圆百里内未发现教育机构！\033[0m".center(60))
                    continue
            elif reply == '2':
                man.Creat()
            else:
                print('\033[0;31;40mWhat!!!\033[0m')
                continue
        else:
            if reply == 'b' or reply == 'q':
                break
            else:
                print('\033[0;31;40mWhat!!!\033[0m')
                continue
if __name__ == "__main__":
    manager_main()