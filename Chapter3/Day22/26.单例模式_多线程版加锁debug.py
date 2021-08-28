import time
import threading


class Singleton:
    instance = None
    lock = threading.RLock()  # 此锁是针对类里面的代码，可以不放在全局变量中，而是放在类变量中

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        with cls.lock:  # 加锁
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance


def task():
    obj = Singleton('x')  # 实例化对象
    print(obj)


for i in range(10):  # 1.有10个任务
    t = threading.Thread(target=task)  # 指定线程任务，等待CPU调度
    t.start()  # 启动线程
