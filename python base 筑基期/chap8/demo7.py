# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 18:04
s1={10,20,30,40}
s2={20,30,10,40}
print(s1==s2)
print(s1!=s2)


s1={10,20,30,50,60,70,80}
s2={10,20,30}
s3={10,20,40}
print(s2.issubset(s1))
print(s3.issubset(s1))

print(s1.issuperset(s2))
print(s1.issuperset(s3))

print(s2.isdisjoint(s3))
s4={100,600,400}
print(s2.isdisjoint(s4))