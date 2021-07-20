# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 22:02
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

# 变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)

# 类的拷贝
print('--------------------------------------------------------------')
disk=Disk()
computer=Computer(cpu1,disk)
# 浅拷贝
import  copy
print(disk)
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
print('---------------------------------------------------------------')
# 深拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)