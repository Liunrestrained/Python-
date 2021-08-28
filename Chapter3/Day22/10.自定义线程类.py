import threading


class MyThread(threading.Thread):  # 相当于继承原来的线程类
    def run(self):  # 执行这个方法
        print("执行此线程", self._args)  # _args就等于下面的args传递的元组


t = MyThread(args=(100,))  # 实例化时，就相当于创建了一个线程
t.start()  # 启动线程，等CPU调用
