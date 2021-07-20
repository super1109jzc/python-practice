# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/16 12:01
'''从键盘录入密码，最多录入三次'''
'''
for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确！')
        break
    else:
        print('密码不正确！！！')
'''
a=0
while a<3:
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确！')
        break
    else:
        print('密码不正确！！！')
    a+=1
