# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/26 19:04
import  sys
import time
import math
import  urllib.request
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('http://www.baidu.com').read())
print(math.pi)