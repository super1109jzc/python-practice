# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 14:40
score={'张三':100,'李四':98,'王五':45}
print('张三' in score)
print('张三' not in score)

del score['张三']
# score.clear()
print(score)

score['陈留']=96
print(score)

score['陈留']=100
print(score)