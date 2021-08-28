import threading

loop = 1000000
number = 0


def _add(count):
    global number
    for i in range(count):
        number += 1


t = threading.Thread(target=_add, args=(loop,))
t.start()  # 当前的线程准备就绪,等待CPU调度，具体时间是由CPU来决定的。

print(number)  # 子线程启动后，会直接执行这一行代码，所以打印的数据是随机的0~1000000。
