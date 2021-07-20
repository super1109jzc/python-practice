# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 19:06
def fun(a,b):
    c=a+b
    print(c)


name='杨'
print(name)
def fun2():
    print(name)
fun2()

def fun3():
    global age   # 局部变量加上global变成全局变量
    age=33
    print(age)
fun3()
print(age)