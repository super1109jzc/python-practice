# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 16:44
class Student:
    native_pace='吉林'  # 类属性
    def __init__(self,name,age):
        self.name=name  # self.name称为实体属性，进行了一个赋值操作，将局部变量name的值赋给实体属性
        self.age=age

    # 实例方法
    def eat(self):
        print('更不能？')

    # 静态方法
    @staticmethod
    def sm():
        print('okjhgfghj')

    # 类方法
    @classmethod
    def vc(cls):
        print('阿斯蒂芬')

# 定义在类之外的称为函数，定义在类之内的称为方法
def et():
    print('jfgh')

# 创建Student类的对象
stu1=Student('张三',20)
'''
print(id(stu1))
print(type(stu1))
print(stu1)
print('-----------------------------------------')
print(id(Student))
print(type(Student))
print(Student)
'''
stu1.eat()
print(stu1.name)
print(stu1.age)

print('-----------------------------------------')
Student.eat(stu1)  # 41行 与 36行，都是调用Student中的eat方法

# 类属性的使用方式
print(Student.native_pace)
stu2=Student('涨十',33)
stu3=Student('哦怕',21)
print(stu2.native_pace)
print(stu3.native_pace)
Student.native_pace='天津'
print(stu2.native_pace)
print(stu3.native_pace)
