# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 18:44
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super(Student, self).info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teacherofyear):
        super().__init__(name,age)
        self.teacherofyear=teacherofyear
    def info(self):
        super(Teacher, self).info()
        print(self.teacherofyear)

stu=Student('张三',20,'1001')
teacher=Teacher('李四',33,10)

stu.info()
teacher.info()