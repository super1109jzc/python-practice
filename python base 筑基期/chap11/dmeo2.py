# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 22:03
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为',result)
finally:
    print('谢谢您的使用')