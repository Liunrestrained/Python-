import threading

loop = 10000000
number = 0


def _add(count):
    global number
    for i in range(count):
        number += 1


def _sub(count):
    global number
    for i in range(count):
        number -= 1


t1 = threading.Thread(target=_add, args=(loop,))
t2 = threading.Thread(target=_sub, args=(loop,))
t1.start()
t2.start()
# 由于GIL锁的限制，每次CPU只能调一个线程。
# 两个线程并不是执行完第一个才执行第二个，而是交替执行一部分，直至执行完。
# 需要注意的是，由于两个线程在交替执行一个变量，由于每次执行过程分片的大小不均，大概率导致数据最后的结果错误。
t1.join()  # t1线程执行完毕,才继续往后走
t2.join()  # t2线程执行完毕,才继续往后走

print(number)  # 结果不确定
