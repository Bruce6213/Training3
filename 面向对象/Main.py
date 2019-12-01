# Author  : Bruce li
# Date    : From 2019/11/22 to 2019/11/30
# Describe: 面向对象综合练习
# Trouble : None



# 角色:学校、学员、课程、讲师
# 要求:
# 1. 创建北京、上海2所学校
# 2. 创建linux ,python, go 3个课程，linux\py 在北京开，go 在上海开
# 3. 课程包含，周期，价格，通过学校创建课程
# 4. 通过学校创建班级， 班级关联课程、讲师
# 5. 创建学员时，选择学校，关联班级
# 5. 创建讲师角色时要关联学校
# 6. 提供两个角色接口
# 6.1 学员视图， 可以注册， 交学费， 选择班级
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
# 6.3 管理视图，创建讲师， 创建班级，创建课程
# 7. 上面的操作产生的数据都通过pickle序列化保存到文件里



# 约定： 'b'表示返回上一个页面
#        'q'表示退出
import class_manager, class_school, class_teacher, class_student
def auto_creat():
    new_school = class_school.School('清华大学', '北京')
    new_school2 = class_school.School('北京大学', '北京')
    class_manager.Manager.schools.append(new_school)
    class_manager.Manager.schools.append(new_school2)
    new_class = class_school.Class(3000.00, 2, 2, 'Linux')
    new_school.school_class.append(new_class)
    new_class2 = class_school.Class(4000.00, 2, 20, 'python')
    new_school2.school_class.append(new_class2)
    teacher = class_teacher.Teacher('Bruce', 25, 'm', 'python', new_school2.name, new_class2)
    new_school2.teachers.append(teacher)
    print('='.center(60, '='))
    print('尊敬的%s老师：' % teacher.name)
    print('您的登入账号为: ', teacher.name)
    passwd = class_manager.Random()
    print('您的登入密码为: %d\n\033[0;30;41m建议你立即修改密码以避免账号被他人非法登入。\033[0m' % passwd)
    teacher.passwd = passwd
    class_manager.teacher_account[teacher.name] = passwd
    print('='.center(60, '='))
    teacher2 = class_teacher.Teacher('Alex', 32, 'm', 'Linux', new_school.name, new_class)
    new_school.teachers.append(teacher2)
    print('尊敬的%s老师：' % teacher2.name)
    print('您的登入账号为: ', teacher2.name)
    passwd = class_manager.Random()
    print('您的登入密码为: %d\n\033[0;30;41m建议你立即修改密码以避免账号被他人非法登入。\033[0m' % passwd)
    teacher2.account = teacher2.name
    teacher2.passwd = passwd
    class_manager.teacher_account[teacher2.name] = passwd
    print('='.center(60, '='))
    print('\n\n\n')
def show():
    global user
    while True:
        print('1、学员入口')
        print('2、讲师入口')
        print('3、管理员入口')
        reply = input('==>')
        if reply.isdigit() and (int(reply) > 0 and int(reply) < 4):
            if int(reply) == 1:
                while True:
                    print('1、登入')
                    print('2、注册')
                    reply = input('==>')
                    if reply.isdigit():
                        if reply == '1':
                            user, passwd = class_student.student_main()
                            host = class_manager.match(1, user, passwd)
                            while True:
                                print('1、查看个人信息')
                                print('2、查看考试成绩')
                                print('3、修改登入密码')
                                reply2 = input('==>')
                                if reply2 == '1':
                                    host.view_information()
                                    class_manager.tips()
                                elif reply2 == '2':
                                    host.mark()
                                    class_manager.tips()
                                elif reply2 == '3':
                                    class_manager.change(0, host)
                                    class_manager.tips()
                                elif reply2 == 'b' or reply2 == 'q':
                                    break
                                else:
                                    print('\033[0;31;40mWhat!!!\033[0m')
                                    continue
                            break
                        elif reply == '2':
                            class_student.Student.register()
                            class_manager.tips()
                        else:
                            print('\033[0;31;40mWhat!!!\033[0m')
                            continue

                    elif reply == 'b' or reply == 'q':
                        break
                    else:
                        print('\033[0;31;40mWhat!!!\033[0m')
                        continue
            elif int(reply) == 2:
                user, passwd = class_teacher.teacher_main()
                host = class_manager.match(0, user, passwd)
                while True:
                    print('1、查看个人信息')
                    print('2、学生成绩')
                    print('3、开始考试')
                    print('4、修改登入密码')
                    reply = input('==>')
                    if reply.isdigit():
                        if reply == '1':
                            host.view_info()
                            class_manager.tips()
                        elif reply == '2':
                            host.score()
                            class_manager.tips()
                        elif reply == '3':
                            host.examination()
                            class_manager.tips()
                        elif reply == '4':
                            class_manager.change(1, host)
                            class_manager.tips()
                        else:
                            print('\033[0;31;40mWhat!!!\033[0m')
                            continue
                    else:
                        if reply == 'b' or reply == 'q':
                            break
                        else:
                            print('\033[0;31;40mWhat!!!\033[0m')
                            continue
            elif int(reply) == 3:
                class_manager.manager_main()
                continue
            else:
                pass
                break
        elif reply == 'b' or reply == 'q':
            break
        else:
            print('\033[0;31;40mWhat!!!\033[0m')
            continue
if __name__ == "__main__":
    auto_creat()
    show()



