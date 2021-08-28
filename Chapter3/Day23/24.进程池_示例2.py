import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor  # 导入进程池(python2有)和线程池(3添加)


def task(num):
    print("执行", num)
    time.sleep(2)


if __name__ == '__main__':
    # 格式写在这里fock,spawn
    pool = ProcessPoolExecutor(4)  # 创建4个进程
    for i in range(10):
        pool.submit(task, i)  # 函数， 参数
        # 默认不会等，进程池内的任务再内部处理，后面的代码直接运行
    pool.shutdown(True)  # 等子进程执行完毕，再继续主进程，类似于“守护线程”
    print(1)
    print(2)
