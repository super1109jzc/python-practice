# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/15 17:34
money=1000
s=int(input('请输入取款金额'))
if money>s:
    money-=s
    print('取款成功，余额为：',money)