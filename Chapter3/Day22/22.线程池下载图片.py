# 导入模块
import os
import requests
from concurrent.futures import ThreadPoolExecutor


def download(file_name, image_url):
    # 下载文件，一定要关梯子
    res = requests.get(url=image_url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })

    if not os.path.exists("images"):  # 目录是否步存在
        os.makedirs("images")  # 创建该目录
    file_path = os.path.join("images", file_name)

    with open(file_path, mode="wb")as f:  # 创建文件打开
        f.write(res.content)  # 将数据写入


# 创建进程池
pool = ThreadPoolExecutor(12)

# 打开本地下载地址源文件
with open("22.mv.csv", mode="rt", encoding="utf-8")as file_object:  # 读取文件
    for line in file_object:  # 循环每一条数据
        nid, name, url = line.split(",")  # 分割每一条数据:编号,名字,链接
        url = url.strip()  # 链接文件后面有换行符，要去掉，不然文件加载不出来
        file_name = "{}.png".format(name)  # 文件名.类型
        pool.submit(download, file_name, url)  # 指定函数，文件名，链接，等待CPU调度线程执行
