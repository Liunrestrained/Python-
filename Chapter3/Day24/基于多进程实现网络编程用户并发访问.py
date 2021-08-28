import socket
import multiprocessing


def task(conn):
    while True:
        client_data = conn.recv(1024)
        data = client_data.decode("utf-8")
        print("收到客户端的消息", data)
        if data.upper() == "Q":
            break
        conn.sendall("收到收到".encode("utf-8"))
    conn.close()


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 1008))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()  # 等待连接，接客
        # 创建子进程，安排一个子进程给访客，去执行task方法，主进程继续回去等待接客
        t = multiprocessing.Process(target=task, args=(conn,))
        t.start()
    sock.close()


if __name__ == '__main__':
    run()