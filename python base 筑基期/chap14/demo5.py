# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/28 16:23
src_file=open('logo.png','rb')
target_file=open('copylogo.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()