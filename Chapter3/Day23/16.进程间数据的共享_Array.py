from multiprocessing import Process, Value, Array


def f(data_array):
    data_array[0] = 66


if __name__ == '__main__':
    arr = Array('i', [11, 22, 33, 44])  # 数组：元素类型必须是int；只能是这么几个数据，不能多，也不能少

    p = Process(target=f, args=(arr, ))
    p.start()
    p.join()

    print(arr[:])  # [66, 22, 33, 44]
