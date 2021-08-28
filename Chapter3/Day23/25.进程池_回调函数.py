import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def task(num):
    print("子任务", multiprocessing.current_process().pid)
    print("执行", num)
    time.sleep(2)
    return num


def done(res):
    print(multiprocessing.current_process().pid)
    time.sleep(1)
    print(res.result())  # 获取task返回对象的值
    time.sleep(1)


if __name__ == '__main__':

    pool = ProcessPoolExecutor(4)  # 创建4个进程
    for i in range(5):  # n个任务要执行
        fur = pool.submit(task, i)  # 等待CPU调度，并获取子进程任务执行后返回的特殊对象
        fur.add_done_callback(done)  # 主进程执行done回调函数。

    print(multiprocessing.current_process().pid)
    pool.shutdown(True)  # 等待子进程
