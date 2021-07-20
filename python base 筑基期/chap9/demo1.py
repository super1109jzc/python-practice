# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/19 16:46
# 字符串驻留机制
a='python'
b="python"
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))

a='abc%'
b='abc%'
print(a is b)
