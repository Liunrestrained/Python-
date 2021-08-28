import time
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def task(lock):
    print("开始")
    # lock.acquire()
    # lock.relase()
    with lock:
        # 假设文件中保存的一个内容就是10
        with open('22.f1.txt', mode="r", encoding="utf-8")as f:
            current_num = int(f.read())

        print("排队抢票了")
        time.sleep(1)
        current_num -= 1

        with open("22.f1.txt", mode="w", encoding="utf-8")as f:
            f.write(str(current_num))


if __name__ == '__main__':
    pool = ProcessPoolExecutor()  # 创建进程
    # lock_object = multiprocessing.RLock()  # 进程池中使用进程锁，需要基于Manager中的Lock和RLock来实现。
    manager = multiprocessing.Manager()
    lock_object = manager.RLock()  # Lock
    for i in range(10):
        pool.submit(task, lock_object)
