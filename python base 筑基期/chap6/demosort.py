# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 1:24
lst=[20,40,10,98,54]
print('排序前的列表',lst)
lst.sort()
print('排序后的列表',lst)
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)

print('-----------------------使用sorted()----------------------')
lst=[20,40,10,98,54]
new_list=sorted(lst)
print(lst)
print(new_list)
desc_list=sorted(lst,reverse=True)
print(desc_list)