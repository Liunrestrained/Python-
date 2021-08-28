import time
import threading


class Singleton:
    instance = None
    lock = threading.RLock()  # 此锁是针对类里面的代码，可以不放在全局变量中，而是放在类变量中

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):

        if cls.instance:  # 为后期重复实例化对象做准备，可以免除加锁释放的过程，减轻性能消耗。
            return cls.instance

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

# 假设后面执行完1000行代码后，我还需要实例化这个Singleton对象一次，按照之前的步骤，仍然需要加锁、判断、归还锁，步骤繁琐，因为此时对象大概率已经存在。
# 因此，直接在加锁前面加上一个判断对象已经存在，则返回该对象的代码。
data = Singleton('一千年以后')
print(data)
