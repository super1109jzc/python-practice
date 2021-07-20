# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 1:09
lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
# lst.remove(100)


lst.pop(1)
print(lst)
# lst.pop(5)
lst.pop()
print(lst)

print('------------------------------------')
'''new_list=lst[1:3]
print(new_list)'''

lst[1:3]=[]
print(lst)

lst.clear()
print(lst)

del lst