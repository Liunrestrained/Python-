import threading
import time


def task(arg):
    time.sleep(5)
    print("任务")


t = threading.Thread(target=task, args=(11,))
t.setDaemon(True)  # True/False
t.start()

print("END")

'''
t.setDaemon(布尔值) 1.守护线程必须放在start之前。
t.setDaemon(True)  2.主线程关闭，子线程也会关闭。
t.setDaemon(False) 3.设置为非守护线程，主线程等待子线程，子线程执行完毕后，主线程才结束。（默认）
'''
