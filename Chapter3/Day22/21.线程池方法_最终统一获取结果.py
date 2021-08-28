import time
import random
from concurrent.futures import ThreadPoolExecutor, Future


def task(video_url):
    print("开始执行任务", video_url)
    time.sleep(2)
    return random.randint(0, 10)  # 返回一个0-10的随机整数


pool = ThreadPoolExecutor(10)  # 创建线程池，最多维护10个线程

future_list = []  # 创建一个空列表，存储每一个线程任务的返回值

url_list = ["www.{}.com".format(i) for i in range(15)]  # 15个任务
for url in url_list:  # 循环将任务分配给线程
    future = pool.submit(task, url)  # 明确任务方法和参数，等待CPU调度，并获取一个返回的特殊对象
    future_list.append(future)  # 将线程任务的这个特殊对象添加到列表

pool.shutdown(True)  # 主线程等待
for fu in future_list:  # 循环列表的特殊对象
    print(fu.result())  # 通过result()拿到它的结果

'''了解一下回调函数'''
