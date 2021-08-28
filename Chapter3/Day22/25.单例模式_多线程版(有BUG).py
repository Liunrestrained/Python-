import time
import threading


class Singleton:
    instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.instance:  # 第一个线程运行时，这个对象肯定没有创建；通常第2个线程开始就会检测到对象已经创建，执行此步骤，沿用一个地址。
            # 但是如果线程1等了0.1秒，没有最快创建这个对象，那就会有一些线程跳过”对象已存在则返回“这一步，继续创建新的对象。导致达不到所有对象使用同一个地址的效果。
            return cls.instance
        time.sleep(0.1)  # 等0.1秒
        cls.instance = object.__new__(cls)
        return cls.instance


def task():
    obj = Singleton('x')  # 实例化对象
    print(obj)


for i in range(10):  # 1.有10个任务
    t = threading.Thread(target=task)  # 指定线程任务，等待CPU调度
    t.start()  # 启动线程
