# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/28 16:45


class MyContenMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')
    def show(self):
        print('show方法被调用执行了')

with MyContenMgr() as file:
    file.show()