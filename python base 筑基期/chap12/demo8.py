# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 19:51
class Animal(object):
    def eat(self):
        print('吃屎')

class Dog(Animal):
    def eat(self):
        print('吃屎球球')

class Cat(Animal):
    def eat(self):
        print('护额的和看见黄瓜')

class Person(object):
    def eat(self):
        print('哈哈哈')

def fun(obj):
    obj.eat()

# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('-----------------------------------')
fun(Person())

