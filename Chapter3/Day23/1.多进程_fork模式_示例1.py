'''该方法仅Mac、Linux系统可以与运行'''
'''编写效率高，代码简洁，但是可读性不及spawn，变量容易混淆；
可以‘拷贝’几乎所有的数据，且支持文件对象、线程锁等的传参。
'''

import multiprocessing


def task():
    print(name)  # []


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # 更换fork模式，会将主进程中的所有内容拷贝一份，速度最快，任意位置开始
    name = []

    p1 = multiprocessing.Process(target=task)
    p1.start()
