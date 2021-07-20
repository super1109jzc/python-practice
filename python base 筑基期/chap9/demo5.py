# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/19 18:59
s='hello world python'


lst=s.split()
print(lst)
s1='hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))

print('-----------------------------------------')


print(s.rsplit())
print(s1.rsplit('|'))
print(s1.rsplit(sep='|',maxsplit=1))