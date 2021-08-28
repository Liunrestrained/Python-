'''等待当前进程的任务执行完毕后再向下继续执行。'''
import time
import multiprocessing
from multiprocessing import Process


def task(arg):
    time.sleep(2)
    print("执行中...")


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    p = Process(target=task, args=('xxx',))
    p.start()
    p.join()

    print("继续执行...")
