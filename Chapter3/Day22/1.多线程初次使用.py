import time
import requests
import threading  # 帮助我创建线程

'''
线程，是计算机中可以被cpu调度的最小单元(真正在工作）。
进程，是计算机资源分配的最小单元（进程为线程提供资源）。

一个进程中可以有多个线程,同一个进程中的线程可以共享此进程中的资源。
'''
'''
def func(a1, a2, a3):
    pass

t = threading.Thread(targer=func, args=(11, 12, 13))
t.start()
'''

url_list = [("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
            ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
            ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
            ]


def task(file_name, video_url):  # 执行函数，接收文件名和链接地址
    res = requests.get(video_url)  # 发送网络请求
    with open(file_name, mode="wb")as f:  # 创建文件并写入
        f.write(res.content)  # 将从网络获取的二进制信息写入文件
    print(time.time())  # 执行本次循环的结束时间


for name, url in url_list:  # 循环下载列表（文件名+下载连接）
    print(time.time())  # 任务开始时间
    t = threading.Thread(target=task, args=(name, url))  # 创建线程，传入待执行函数和函数参数
    t.start()  # 启动
