# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 17:55
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')
print('----------------------------------------------------------')
stu1=Student('张三',22)
stu2=Student('李四',33)
print(id(stu1))
print(id(stu2))
print('------------------为stu2动态绑定性别属性----------------------')
stu2.gender='女'
print(stu1.name,stu2.age)
print(stu2.name,stu2.age,stu2.gender)
print('-----------------------------------------------------------')
stu1.eat()
stu2.eat()

def show():
    print('定义在类之外的，称为函数')
stu1.show=show
stu1.show()

