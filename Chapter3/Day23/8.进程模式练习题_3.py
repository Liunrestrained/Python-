'''win不能执行'''
import time
import threading
import multiprocessing


def func():
    print("来了")
    with lock:
        print(666)
        time.sleep(1)


def task():
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
    time.sleep(2)


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # 更改fork模式  # 锁被拷贝到子进程后，锁的对象是子进程中除了主进程以外的其它进程。
    name = []
    lock = threading.RLock  # 创建一把锁
    lock.acquire()  # 加锁

    p1 = multiprocessing.Process(target=task)  # 执行子进程，该子进程将全部数据拷贝后，子进程对自己而言就是主进程，可以在这个子进程中创建属于它的子线程或子进程，所拷贝的锁将会对它的除了主进程之外的其它进程产生作用。
    p1.start()
