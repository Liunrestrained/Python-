import multiprocessing


def task():
    print(name)
    file_object.write("他媳妇\n")  # 5.写入文件对象到内存
    file_object.flush()  # 刷入硬盘


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")  # win不能执行
    # 此处全部数据拷贝了一份
    name = []
    file_object = open("x1.txt", mode="a+", encoding="utf-8")
    file_object.write("张律师\n")  # 1.主线程将文件对象写入内存  4.内存中没有文件对象
    file_object.flush()  # 2.文件对象被从内存刷入硬盘

    p1 = multiprocessing.Process(target=task)  # 3.开始执行，数据全部拷贝一份
    p1.start()


'''
文件中的内容：
张律师
他媳妇
'''