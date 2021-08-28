import os  # 路径
import time  # 时间
import threading  # 操作线程
import multiprocessing  # 操作进程


def func():
    time.sleep(3)


def task(arg):
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
    # 获取进程或子进程ID
    print("当前子进程ID：", os.getpid()), print("当前父进程ID：", os.getppid())  # 当前主进程的ID,当前父进程ID
    # print(os.getpid()), print(os.getppid())  # 当前主进程的ID,当前父进程ID
    # 获取线程个数（主线程+子线程）
    print("线程个数：", len(threading.enumerate()))
    time.sleep(2)
    # 获取进程和进程名字
    print("当前进程的名字：", multiprocessing.current_process().name)  # 获取当前进程.名字


if __name__ == '__main__':
    print("当前进程ID：", os.getpid())  # 当前主进程的ID
    multiprocessing.set_start_method("spawn")
    p = multiprocessing.Process(target=task, args=("xxx",))
    # 进程名字起名
    p.name = "你猜我叫啥"  # 起名要写在start前面
    p.start()

    print("继续执行")
