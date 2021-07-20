# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/17 20:35
'''创建列表的第一种方式，使用【】'''
lst=['hello','world',98,'hell0']
print(lst)
print(lst[0],lst[-3])
'''创建列表的第二种方式，使用内置函数list（）'''
lst2=list(['hello','world',98])

lst3=['hello','world',98,'hello','world',234]
print(lst3[2])
print(lst3[-3])
# print(lst[10])


lst4=[10,20,30,40,50,60,70,80]
print(lst4[1:6:1])
print(lst4[1:6])
print(lst4[1:6:])
print(lst4[:6:2])
print(lst4[::-1])