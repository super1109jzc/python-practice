# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/26 18:39

# 在demo5中导入calc自定义模块使用
import  calc
print(calc.add(10,20))
from calc import add
print(add(20,60))