# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/28 16:32
file=open('c.txt','a')
file.write('hello')
lst=['java','go','python']
file.writelines(lst)
file.close()