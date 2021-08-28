import threading

number = 0


def _add():
    global number
    for i in range(1000000):
        number += 1


def _sub():
    global number
    for i in range(1000000):
        number -= 1


t1 = threading.Thread(target=_add)
t2 = threading.Thread(target=_sub)

t1.start()
t1.join()

t2.start()
t2.join()

print(number)
