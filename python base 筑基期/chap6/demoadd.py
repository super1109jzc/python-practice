# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 0:45
lst=[10,20,30]
lst.append(100)
print(lst)

lst2=['hello','world']
'''lst.append(lst2)
print(lst)'''
lst.extend(lst2)
print(lst)

lst.insert(1,90)
print(lst)

lst3=['True','False','fuck']
lst[1:]=lst3
print(lst)

