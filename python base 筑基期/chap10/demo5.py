# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 18:34
def fun(*args):  # 函数定义时  个数可变的位置参数  只能有一个
    print(args)
    print(args[0])

fun(10)
fun(20,60)
fun(41,62,33)


def fun1(**args):    # 函数定义时  个数可变的关键字参数   只能有一个
    print(args)


fun1(s=10)
fun1(s4=33,s2=66,s0=65)

def fun2(*args1,**args2):
    pass

'''def fun3(**args1,+args):
    pass
    当同时有  个数可变的位置参数  和  个数可变的关键字参数 时
    要求  个数可变位置形参   放在   个数可变的关键字形参  前
'''
