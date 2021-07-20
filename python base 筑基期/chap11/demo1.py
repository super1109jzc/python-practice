# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 21:50
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
    print(result)
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')