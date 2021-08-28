import threading

data_list = []

lock_object = threading.RLock


def task():
    print("开始")
    for i in range(10000000):
        data_list.append(i)
    print(len(data_list))
    # 19120249
    # 20000000  # 最终的结果是正确的


for i in range(2):
    t = threading.Thread(target=task)
    t.start()

'''
Python中带锁的操作有：
L.append(x)
L1.extend(L2)
x = L[i]
x = L.pop
L1[i:j] = L2
L.sort()
x = y
x.field = y
D[x] = y
D1.update(D2)
D.keys()
'''
'''
Python中不带锁的操作有：
i = i+1
L.append(L[-1])
L[i] = L[j]
D[x] = D[x] + 1
'''
