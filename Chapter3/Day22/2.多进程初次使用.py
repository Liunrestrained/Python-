import time
import requests
import multiprocessing  # 创建进程

# 多进程比多线程的开销要大。
# 创建的进程当中，会创建一个线程；一个进程中至少有一个线程干活！
# t = multiprocessing.Process(target=函数名, args=(name, url))
# t.start()

url_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]


def task(file_name, video_url):
    res = requests.get(video_url)
    with open(file_name, mode="wb")as f:
        f.write(res.content)
    print(time.time())


if __name__ == '__main__':
    print(time.time())  # 进程模式下，将这个时间代码放在里面
    # windows支持spawn, mac支持fork和spawn,linux用fork.(python3.8开始默认设置spawn)不同的系统，创建进程的机制不一样。
    # multiprocessing.set_start_method('fork')更改模式。
    for name, url in url_list:
        t = multiprocessing.Process(target=task, args=(name, url))
        t.start()


'''# 程序会报错
print(time.time())
for name, url in url_list:
    t = multiprocessing.Process(target=task, args=(name, url))
    t.start()
'''