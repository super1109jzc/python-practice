# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 17:10
t=(10,[20,30],9)
print(t)
print(type(t),id(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

print(id(100))
# t[1]=100
t[1].append(100)
print(t,id(t))