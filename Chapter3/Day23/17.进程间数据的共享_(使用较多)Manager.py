from multiprocessing import Process, Manager


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(666)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()  # 创建一个字典
        l = manager.list()  # 创建一个列表

        p = Process(target=f, args=(d, l))  # 创建一个子进程
        p.start()  # 启动
        p.join()  # 等待子进程执行结束

        print(d)
        print(l)
