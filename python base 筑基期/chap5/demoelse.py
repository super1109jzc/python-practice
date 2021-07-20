# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/16 12:47
'''
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确！！！')
        break
    else:
        print('密码不正确！！！')
else:
    print('对不起，三次密码均错误！')
'''

a=0
while a<3:
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确！！！')
        break
    else:
        print('密码不正确！！！')
    a+=1
else:
    print('对不起，三次密码均错误！')
