import threading
import requests


class DouYinThread(threading.Thread):  # 继承原线程类对象
    def run(self):  # 执行方法
        file_name, video_url = self._args
        res = requests.get(video_url)
        with open(file_name, mode="wb")as f:
            f.write(res.content)


url_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]

for item in url_list:
    t = DouYinThread(args=(item[0], item[1]))  # 实例化类的对象
    t.start()  # 启动，等待CPU调度
