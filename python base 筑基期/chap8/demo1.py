# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/18 16:26
'''可变序列  列表  字典'''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))

'''不可变序列 字符串 元组'''
s='hello'
print(id(s))
s=s+' world'
print(id(s))