# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/16 11:41
for item in 'Python':
    print(item)

for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为“-”
for _ in range(5):
    print('人生苦短，我用python')

print('使用for循环，计算1-100之间的偶数和')
sum=0
for item in range(1,101):
    if item%2==0:
        sum+=item
print('1到100之间的偶数和为',sum)

print('使用for循环，计算100-999之间的水仙花数')
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if ge**3+shi**3+bai**3==item:
        print('水仙花数为：',item)
