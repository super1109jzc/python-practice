# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 18:55

def fun(a,b=10):     # b称为默认值形参
    print('a=',a)
    print('b=',b)

def fun2(*args):
    print(args)
def fun3(**args2):
    print(args2)
fun2(10,20,30,50)
fun3(a=11,b=22,c=33,d=44)


def fun4(a,b,*,c,d):  # 从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

# 调用fun4函数
# fun4(10,20,30,40)
fun4(a=10,b=20,c=60,d=1)
fun4(10,20,c=22,d=65)


'''函数定义时的形参的顺序问题'''
def fun5(a,b,*,c,d,**args):
    pass

def fun6(*args,**srgs1):
    pass

def fun7(a,b=10,*args,**args1):
    pass
