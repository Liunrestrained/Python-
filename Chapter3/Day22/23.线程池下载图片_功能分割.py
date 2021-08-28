# 导入模块
import os
import requests
from concurrent.futures import ThreadPoolExecutor


def download(image_url):
    # 下载文件，一定要关梯子
    res = requests.get(url=image_url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })
    return res


def outer(file_name):
    def save(response):
        res = response.result()  # 获取网络请求的返回值
        if not os.path.exists("images"):  # 目录是否步存在
            os.makedirs("images")  # 创建该目录

        file_path = os.path.join("images", file_name)

        with open(file_path, mode="wb")as f:  # 创建文件打开
            f.write(res.content)  # 将数据写入

    return save


# 创建进程池
pool = ThreadPoolExecutor(12)

# 打开本地下载地址源文件
with open("22.mv.csv", mode="rt", encoding="utf-8")as file_object:  # 读取文件
    for line in file_object:  # 循环每一条数据
        nid, name, url = line.split(",")  # 分割每一条数据:编号,名字,链接
        url = url.strip()  # 文件后面的换行符一定要去掉，否则图片加载不出来
        file_name = "{}.png".format(name)  # 文件名.类型
        fur = pool.submit(download, url)  # 指定函数，链接，等待CPU调度线程执行,并获取线程执行后任务返回的对象
        fur.add_done_callback(outer(file_name))  # 执行(执行outer(file_name)这个函数返回save函数)save函数，将含有下载结果的对象传递进去解析
