import socket

# 1.监听本机的IP地址
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket对象
sock.bind(("127.0.0.1", 8001))  # 获取本机的IP、端口
sock.listen(5)  # 支持等待排队的人数5人

while True:
    conn, addr = sock.accept()  # 2.阻塞，等待访客连接

    client_data = conn.recv(1024)  # 3.阻塞，等待客户端发来信息，并且每次最多接收1024字节
    print(client_data.decode("utf-8"))  # 4.将接收的信息通过utf-8编码，转换成字符串格式

    conn.sendall("hello world".encode("utf-8"))  # 5.回复访客的消息，通过utf-8编码，转换成字节格式

    conn.close()  # 6.关闭连接

# 7.停止服务端程序
sock.close()
