# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/28 16:35
file=open('a.txt','r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()