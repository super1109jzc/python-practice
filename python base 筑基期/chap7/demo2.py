# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 14:36
score={'张三':100,'李四':98,'王五':45}
print(score['张三'])
# print(score['张四'])


print(score.get('张三'))
print(score.get('张四'))
print(score.get('张其',99))