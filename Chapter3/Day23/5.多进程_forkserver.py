'''使用上和spawn一样，windows不能用，只有部分的unix可以用
run参数传必备资源；不支持文件对象/线程锁等传参。通用性最差。
'''
import time
import multiprocessing


def task(data):
    print(data)


if __name__ == '__main__':
    multiprocessing.set_start_method("forkserver")  # main代码块开始，run参数传必备资源，CPU在执行时，本质上是在执行这个run方法
    name = []  # 不会被拷贝

    p1 = multiprocessing.Process(target=task, args=(name,))  # 需要将参数主动传递
    p1.start()

    time.sleep(3)
    print(name)
