# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/16 11:27



'''
a=1
while a<10:
    print(a)
    a+=1
'''

'''
a=0
sum=0
while a<5:
    sum+=a
    a+=1
print('和为',sum)
'''

a=1
sum=0
while a<=100:
    if not a%2:
        sum+=a
    a+=1
print('偶数和为',sum)
