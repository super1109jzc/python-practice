# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/19 19:07
s='hello world'
print(s.isidentifier())
print('hello'.isidentifier())
print('张三'.isidentifier())
print('张三_123'.isidentifier())

print('\t'.isspace())

print('abc'.isalpha())
print('张三'.isalpha())
print('张三12'.isalpha())

print('123'.isdecimal())
print('123四'.isdecimal())

print('123'.isnumeric())
print('123四'.isnumeric())

print('abc'.isalnum())
print('张三123'.isalnum())
print('张三！12'.isalnum())