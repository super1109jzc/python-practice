# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 19:34
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字叫{0}，今年{1}岁'.format(self.name,self.age)
stu=Student('张安',20)
print(dir(stu))
print(stu)
print(type(stu))