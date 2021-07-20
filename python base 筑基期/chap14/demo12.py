# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/28 16:54
with open('logo.png','rb') as src_file:
    with open('copy2logo.png','wb') as target_file:
        target_file.write(src_file.read())