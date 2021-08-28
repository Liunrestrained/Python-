import time
import random
from concurrent.futures import ThreadPoolExecutor, Future


def task(video_url):
    print("开始执行任务", video_url)
    time.sleep(2)
    return random.randint(0, 10)


def done(response):
    print("任务执行后的返回值", response.result())  # 对象.result()获取结果


pool = ThreadPoolExecutor(10)  # 创建线程池，维护10个线程

url_list = ["www.{}.com".format(i) for i in range(50)]  # 50个任务
for url in url_list:  # 将10个线程分配给任务，没分到的就等待归还
    future = pool.submit(task, url)  # 任务方法和参数，等待CPU调度，并获取返回的一个特殊的对象，而不是返回的结果
    future.add_done_callback(done)  # 执行该方法，就可以拿到这个特殊对象，并对它进行一些自定义的操作

# 可以做分工，text下载，done将下载的内容写入
