# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/25 18:27
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已经启动')


car=Car('宝马x5')
car.start()
print(car.brand)