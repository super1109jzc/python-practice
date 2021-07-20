# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/14 14:41
# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('hello world')
print("hello world")

# 输出含有运算符的表达式
print(3+1)

# 将数据输出到文件当中,注意点：1.所指定的盘符要存在2.要使用file= fp=
fp=open('D:/text.txt','a+')  # a+ 如果文件不存在就创建，存在就在文件后面继续添加
print('hello world',file=fp)
fp.close()

# 不进行换行输出（输出内容在一行中）
print('hello','world','python')

