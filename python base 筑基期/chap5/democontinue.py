# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/16 12:40

for item in range(1,51):
    if item%5==0:
        print(item)

print('--------------------使用continue---------------')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)