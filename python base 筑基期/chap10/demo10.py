# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 19:18
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(6))

print('-----------------输出前六项----------------')
for i in range(1,7):
    print(fib(i))
