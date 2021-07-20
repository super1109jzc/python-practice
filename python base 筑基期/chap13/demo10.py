# 编 程 人    ：小生江子川
# 开 发 时 间 ：2021/1/26 19:19
import schedule
import time
def job():
    print('结婚后。。。')
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)