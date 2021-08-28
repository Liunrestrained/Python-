'''进程锁针对解决的是和线程锁同样的错误情况，也就是多个进程处理同一个数据或文件，导致数据出现错误'''

import time
import multiprocessing  # 创建进程


def task(lock):
    # 假设文件中保存的内容就是一个值：10
    print("开始了")  # 第2个进程开始堵在这里
    lock.acquire()  # 加锁

    with open("22.f1.txt", mode="r", encoding="utf-8")as f:
        current_num = int(f.read())  # 读文件中的数字

    print("排队抢票了")
    time.sleep(0.5)
    current_num -= 1

    with open("22.f1.txt", mode="wt", encoding="utf-8")as f:
        f.write(str(current_num))  # 将减了1的结果覆盖写入文件
    lock.release()  # 释放锁


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  # spawn多进程模式
    lock = multiprocessing.RLock()  # 创建进程锁

    for i in range(10):  # 10个进程执行任务
        p = multiprocessing.Process(target=task, args=(lock,))  # 确定任务，将进程锁传递给子进程(不能传递线程锁)
        p.start()  # 启动，等待CPU调动
    # 这里不能用join，否则会变成单线程执行。可以尝试理解为：这里加上join后，进程得一个一个创建，再执行，效率低下。
    # spawn模式需要这个特殊处理,等候子线程执行完，否则会报错，fock就不需要
    time.sleep(7)
