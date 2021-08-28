import threading


def task(arg):
    name = threading.current_thread().getName()
    # name = 获取当前执行此代码的线程.它的名字
    print(name)


for i in range(5):
    t = threading.Thread(target=task, args=(11,))
    t.setName("神州-{}-号".format(i))  # 名字随便取，格式任意
    t.start()
