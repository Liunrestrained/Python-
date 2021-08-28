'''python3正式提供线程池'''
'''创建过多的线程池会导致线程切换频率过多，反而降低执行效率'''

'''使用线程池'''
import time
from concurrent.futures import ThreadPoolExecutor


def task(video_url, num):
    print("开始执行任务", video_url)
    time.sleep(5)


pool = ThreadPoolExecutor(10)  # 创建线程池，最多维护10个线程

url_list = ["xxx.{}.com".format(i) for i in range(300)]

for url in url_list:  # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行任务，执行完毕后再将线程归还；如果没有空闲的线程，则等待。
    pool.submit(task, url, 2)  # 函数名，参数，参数，...

print("END")
