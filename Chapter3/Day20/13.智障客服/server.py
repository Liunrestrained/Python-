import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1.实例化socket对象
sock.bind(("127.0.0.1", 8001))  # 获取自己的IP和端口
sock.listen(5)  # 容纳排队的人数

while True:
    conn, addr = sock.accept()  # 阻塞，等待访客发起连接
    print('检测到访客连接')

    conn.sendall("欢迎访问服务系统，请输入你要办理的业务！".encode("utf-8"))

    while True:
        data = conn.recv(1024)  # 阻塞，等待访客的输入，每次最多接收1024字节
        if not data:  # 输入的内容为空
            break  # 结束循环，并断开连接
        data_string = data.decode("utf-8")
        print(data_string)

        conn.sendall("你说啥？".encode("utf-8"))
    print("断开连接了")
    conn.close()

sock.close()
