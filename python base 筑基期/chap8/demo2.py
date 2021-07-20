# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 16:31
t=('python','world',98)
print(t)
print(type(t))

t1=tuple(('python','world',98))
print(t1)
print(type(t1))

t3='python','world',98
print(t3)
print(type(t3))

t4=('python')
print(t4)
print(type(t4))

t5=('python',)
print(t5)
print(type(t5))

'''空创建'''
lst=[]
lst1=list()

d={}
d1=dict()

t6=()
t7=tuple()

print('空列表',lst,lst1)
print('空字典',d,d1)
print('空元组',t6,t7)