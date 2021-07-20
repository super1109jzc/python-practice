# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/28 16:40
file=open('d.txt','a')
file.write('hello')
file.flush()
file.write('world')
file.close()