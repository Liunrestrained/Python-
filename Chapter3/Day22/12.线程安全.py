import threading

lock_object = threading.RLock()  # 创建一把公共锁，必须放在全局变量中，否则没有意义

loop = 1000000
number = 0


def _add(count):
    lock_object.acquire()  # 申请锁，获取后加锁。第一个优先获取，释放后第二个才可以重新获取

    global number
    for i in range(count):
        number += 1
    lock_object.release()  # 释放锁


def _sub(count):
    lock_object.acquire()  # 申请锁

    global number
    for i in range(count):
        number -= 1
    lock_object.release()  # 释放锁


t1 = threading.Thread(target=_add, args=(loop,))
t2 = threading.Thread(target=_sub, args=(loop,))

t1.start()
t2.start()

t1.join()
t2.join()

print(number)
