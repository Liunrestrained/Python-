import os
import time
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor


def task(file_name):
    ip_set = set()  # 已访问的用户量(不重复)
    total_count = 0  # 总访问量
    ip_count = 0  # 用户的单个访问量
    file_path = os.path.join("30.files", file_name)  # 文件路径拼接
    file_object = open(file_path, mode="r", encoding="utf-8")  # 打开路径下的该文件
    for line in file_object:  # 循环读取该文件
        if not line.strip():
            continue
        user_ip = line.split("- -", maxsplit=1)[0].split(",")[0]  # 分割出第一个IP
        total_count += 1  # 总访问量+1
        if user_ip in ip_set:  # 如果该IP已经访问过了，就跳过他，不再操作
            continue
        ip_count += 1  # 单用户访问量+1
        ip_set.add(user_ip)  # 将已经访问过的用户添加到集合(集合无序、可变、数据不重复)
    return {"total": total_count, "ip": ip_count}  # 将总访问量和单用户访问量的字典作为一个特殊对象返回


def outer(info, file_name):
    def done(res, *args, **kwargs):
        info[file_name] = res.result()

    return done


def run():
    info = {}  # 创建一个空字典,可以多进程传递
    pool = ProcessPoolExecutor(4)  # 创建进程池，最多维护4个子进程。
    for file_name in os.listdir("30.files"):  # 读取目录下的每一个文件。
        fur = pool.submit(task, file_name)  # 将方法和字典名字传递给子进程，并获取返回值
        fur.add_done_callback(outer(info, file_name))  # 用回调函数的方法，将对象传入，最后将字典名，键值对写入

    pool.shutdown(True)  # 主进程等待子进程
    for k, v in info.items():
        print(k, v)


if __name__ == '__main__':
    run()
