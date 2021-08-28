'''等待线程池的任务执行完毕'''
import time
from concurrent.futures import ThreadPoolExecutor


def task(video_url):
    print("开始执行任务", video_url)
    time.sleep(3)


pool = ThreadPoolExecutor(10)  # 创建线程池，最多维护10个线程

url_list = ["www.xxx-{}.com".format(i) for i in range(50)]
for url in url_list:  # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行任务，执行完毕后再将线程归还；如果没有空闲的线程，则等待。
    pool.submit(task, url)  # 函数名，参数，参数，...

print("执行中")
pool.shutdown(True)  # 主线程在此等待子线程全部执行完毕，再往下走。类似于线程方法join()
print("继续往下走")
