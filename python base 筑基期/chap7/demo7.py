# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 15:00
item=['fuck','lkj','oiu']
value=[60,20,88]
d={ item.upper():value  for item,value in zip(item,value)  }
print(d)