# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 17:35
s={10,20,30,405,50}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

s.add(80)
print(s)
s.update({200,845,965})
print(s)
s.update([12,62,33])
s.update((14,78,89))
print(s)

s.remove(405)
print(s)
# s.remove(500)
# print(s)

s.discard((845))
print(s)
s.discard(20000)
print(s)

s.pop()
print(s)
s.pop()
print(s)

s.clear()
print(s)