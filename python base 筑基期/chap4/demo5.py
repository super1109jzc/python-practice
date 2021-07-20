# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/15 21:57
num_a=int(input('请输入第一个整数：'))
num_b=int(input('请输入第二个整数：'))
# 比较大小
'''if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)'''

print('使用条件表达式进行比较')
print((num_a,'大于等于',num_b) if num_a>=num_b else (num_a,'小于',num_b))
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))