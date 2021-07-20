# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/15 13:37
a=b=c=20 # 链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('----------支持参数赋值----------')
a=20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a)
a/=3
print(a)
a//=2
print(a)
a,b,c=20,30,40
print(a,b,c)
print('-------------交换两个变量的值----------')
a,b=10,20
print('交换之前',a,b)
# 交换
a,b=b,a
print('交换之后',a,b)