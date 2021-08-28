'''windows、linux都可以用。
run参数传必备资源，不能拷贝，所以代码相对fork要多一点，但是可读性优于fork。
'''
import time
import multiprocessing


def task(data):
    print(data)


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  # main代码块开始，run参数传必备资源，CPU在执行时，本质上是在执行这个run方法
    name = []  # 不会被拷贝

    p1 = multiprocessing.Process(target=task, args=(name,))  # 需要将参数主动传递
    p1.start()

    time.sleep(3)
    print(name)
