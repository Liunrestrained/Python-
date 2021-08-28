import threading

num = 0
lock_object = threading.RLock()


def task():
    print("开始")
    with lock_object:  # 基于上下文管理，内部自动执行acquire和release
        global num
        for i in range(10000000):
            num += 1
    print(num)


for i in range(2):
    t = threading.Thread(target=task)
    t.start()
