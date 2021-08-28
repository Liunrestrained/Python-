import time
import multiprocessing


def task(lock):
    print("开始")
    lock.acquire()
    # 假设文件中保存的内容就是一个值：10
    with open('22.f1.txt', mode='r', encoding='utf-8') as f:
        current_num = int(f.read())

    print("排队抢票了")
    time.sleep(1)
    current_num -= 1

    with open('22.f1.txt', mode='w', encoding='utf-8') as f:
        f.write(str(current_num))
    lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    lock = multiprocessing.RLock()
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(lock,))
        p.start()
# fork的尾部不需要特殊处理
