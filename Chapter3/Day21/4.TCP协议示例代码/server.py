import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建一个服务端，socket.SOCK_DGRAM这个参数与客户端不一样
sock.bind(("127.0.0.1", 8001))
sock.listen(5)

while True:
    conn, addr = sock.accept()  # 阻塞状态，需要等待创建连接

    client_data = conn.recv(1024)
    print(client_data)
    conn.sendall(b"hello world")  # 简化.encode("utf-8")

    conn.close()

sock.close()
