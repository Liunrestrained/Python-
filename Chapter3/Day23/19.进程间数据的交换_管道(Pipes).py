import time
import multiprocessing


def task(conn):
    time.sleep(1)
    conn.send([111, 22, 33, 44])  # 发送主进程信息
    data = conn.recv()  # 阻塞，等待接收主进程信息
    print("子进程接收", data)  # 接收主进程信息
    time.sleep(2)


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()  # 创建一对管道(双向同行)

    p = multiprocessing.Process(target=task, args=(child_conn,))  # 将任意一根管道交给子进程
    p.start()

    info = parent_conn.recv()  # 阻塞，等待接收子进程信息
    print("主进程接收", info)  # 接收子进程信息
    parent_conn.send(666)  # 发送子进程信息
