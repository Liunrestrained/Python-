'''
守护进程（必须放在start之前）.
True:设置为守护进程，主进程执行完毕后，子进程也自动关闭。
False:设置为非守护进程，主进程等待子进程，子进程执行完毕后，主进程才结束。
'''

import time
import multiprocessing
from multiprocessing import Process


def task(arg):
    time.sleep(2)
    print("执行中")


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    p = Process(target=task, args=("xxx"))
    p.daemon = True
    p.start()

    print("继续执行")
