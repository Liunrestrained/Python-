import multiprocessing


def task(q):
    for i in range(10):
        q.put(i)


if __name__ == '__main__':
    queue = multiprocessing.Queue()  # 在主进程中创建一个队列，基于队列可以实现进程之间的数据共享，所以也可以在主进程put，在子进程get。

    p = multiprocessing.Process(target=task, args=(queue,))  # 将队列传递给子进程
    p.start()
    p.join()

    print("主进程")
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
