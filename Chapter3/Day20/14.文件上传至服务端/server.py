import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket对象
sock.bind(("127.0.0.1", 8001))  # 检测自己的IP和端口
sock.listen(5)  # 容纳最大排队人数

conn, addr = sock.accept()  # 阻塞，等待访客发起连接，指代IP和端口

data = conn.recv(1024)  # 接收访客的信息，每次最大接收1024字节，但是每次接收的大小可能不样
total_file_size = int(data.decode("utf-8"))  # 将接收到的文件字节大小转换为整型
# 文件的大小信息，用以确认文件接收以及整合的完整性
file_object = open("xxx.png", mode="wb")  # 打开文件
recv_size = 0

while True:
    data = conn.recv(1024)  # 接收单次发送的字节文件，且每次接收最大1024字节
    file_object.write(data)  # 将接收的文件字节信息写入文件中
    file_object.flush()  # 将文件信息从内存刷入硬盘

    recv_size += len(data)  # 将本次循环接收的字节大小，加在总接收数据上

    if recv_size == total_file_size:  # 总接收数据大小，等于预知的文件大小
        break  # 接收完毕，循环结束

conn.close()  # 结束连接
sock.close()  # 直接关闭服务端（代码中没有总循环，所以是一次性执行）
