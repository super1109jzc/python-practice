# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/15 17:49
score=int(input('请输入一个成绩：'))
if 90<=score<=100:
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
elif score>=0 and score<=59:
    print('E')
else:
    print('对不起，成绩有误，不在成绩的有效范围')