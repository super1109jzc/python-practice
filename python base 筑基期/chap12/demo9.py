# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 19:59
# print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
#  创建一个C类的对象
x=C('Jack',22)   # x是C类型的一个实例对象
print(x.__dict__)  # 实例对象的属性字典
print('----------------------------------------------')
print(x.__class__)   # 输出了对象所属的类
print(C.__bases__)   # 输出了C类的父亲类型的元素
print(C.__base__)    # 类的基类
print(C.__mro__)     # 查看了类的层次结构
print(A.__subclasses__())   # 子类的列表