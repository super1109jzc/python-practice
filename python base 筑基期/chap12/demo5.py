# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 18:32
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age   # 年龄不希望在类的外部被使用，所以加了两个-
    def show(self):
        print(self.name,self.__age)


stu=Student('张三',20)
stu.show()
print(stu.name)

# print(dir(stu))
print(stu._Student__age)   # 在类的外部可以通过 _Student__age 进行访问
