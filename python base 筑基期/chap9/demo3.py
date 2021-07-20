# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/19 18:35
s='hello,python'
a=s.upper()
print(a,id(a))
print(s,id(s))
b=s.lower()
print(b,id(b))
print(s,id(s))
print(b==s)
print(b is s)


s2='hello,Python'
print(s2.swapcase())
print(s2.title())