import threading

number = 0


def _add():
    global number
    for i in range(100000000):
        number += 1


t = threading.Thread(target=_add())
t.start()

t.join()  # 主线程等待子线程执行完
print(number)
