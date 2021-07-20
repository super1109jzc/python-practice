# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 16:37
print(bool(0))
print(bool(66))

def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst=[10,29,34,23,44,53,55]
print(fun(lst))


'''
如果函数返回值只有一个，直接返回类型
如果函数返回值有多个，返回类型为元组
'''