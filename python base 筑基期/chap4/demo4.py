# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/15 21:46
answer=input('您是会员吗？')
money=float(input('请输入您的购物金额'))
if answer=='y':
    if money>=200:
        print('付款金额为：',money*0.8)
    elif money>=100:
        print('付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为：',money)
else:
    if money>=200:
        print('付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)