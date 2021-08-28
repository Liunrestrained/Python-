import multiprocessing


def task():
    print(name)
    file_object.write("他媳妇\n")  # 3.子线程将文件对象写入内存；
    file_object.flush()  # 4.将2和3内内存刷入硬盘


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # win不能执行
    # 此处全部数据拷贝了一份
    name = []
    file_object = open("x1.txt", mode="a+", encoding="utf-8")
    file_object.write("张律师\n")  # 1.主线程将文件对象写入内存；2.子线程拷贝了一份文件对象；

    p1 = multiprocessing.Process(target=task)  # 开始执行子线程的内容
    p1.start()
    # 子线程执行完毕，将1刷入硬盘。


'''
文件中的内容：
张律师
他媳妇
张律师
'''