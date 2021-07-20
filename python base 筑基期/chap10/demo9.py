# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 19:12
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))