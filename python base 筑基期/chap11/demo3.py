# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/24 22:21
# print(10/0)
import traceback
try:
    print('1.----------------------------------------------------')
    print(1/0)
except:
    traceback.print_exc()