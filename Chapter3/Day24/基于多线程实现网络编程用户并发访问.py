import socket  # 实现网络编程
import threading  # 创建线程


def task(conn):
    while True:
        client_data = conn.recv(1024)
        data = client_data.decode("utf-8")
        print("收到客户端发来的消息：", data)
        if data.upper() == "Q":
            break
        conn.sendall("收到收到".encode("utf-8"))
    conn.close()


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 1008))  # 获取本设备的IP、端口。
    sock.listen(5)  # 本服务端最多容纳5个访问者排队。
    while True:
        # 等待客户端来连接。（主线程）
        conn, addr = sock.accept()  # 主线程一直在这里等待用户的访问，收到访问后，向下运行为每个访问者分配一个子线程，主线程则回来继续等待访问。
        # 创建子线程。基于此方法，实现网络编程和并发编程的结合。
        t = threading.Thread(target=task, args=(conn,))
        t.start()

    sock.close()


if __name__ == '__main__':
    run()
