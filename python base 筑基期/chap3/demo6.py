# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/15 16:26
# 比较运算符的结果为bool类型
a,b=10,20
print('a>b吗？',a>b)
print('a<=b吗？',a<=b)


a=10
b=10
print(a==b)        # True 说明，a与b的value相等
print(a is b)      # True 说明，a与b的id标识相同

# 以下代码没学过，后面会给大家讲解
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))

print(a is not b)
print(lst1 is not lst2)
