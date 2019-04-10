# 包含一个学生的类
# 一个sayhello 的函数
# 一个打印语言

class Student():
    def __init__(self, name = "NoName" , age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def sayHello():
        print("Hi,欢迎来到长春大学！  ")

# 此判断语句建议一直作为程序的入口（编程习惯的问题）
if __name__ == '__main__':
    print("我是模块P01呀，你他吗叫我干毛 ！")
