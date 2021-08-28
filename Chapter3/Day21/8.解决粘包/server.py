import socket  # 网络编程模块
import struct  # 处理粘包模块

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket对象，创建服务端
sock.bind(("127.0.0.1", 8001))  # 检测自己的IP、端口
sock.listen(5)  # 最大排队人数
conn, addr = sock.accept()  # 阻塞，访客的IP和mac

# 第一条数据
header1 = conn.recv(4)  # 固定读取4个字节
data_length1 = struct.unpack('i', header1)[0]  # 读取头部，获取数据的大小
has_recv_len = 0  # 已接收的字节大小
data_1 = b""  # 目前总共读取的字节形式文件
while True:  # 循环读取文件
    length = data_length1 - has_recv_len  # 预知的总字节大小，减去已接收的字节大小，剩余待接收字节的大小
    if length > 1024:  # 待接收字节大小 > 1024
        lth = 1024  # 则本次读取最大1024字节
    else:
        lth = length  # 否则本次直接读取剩余大小的字节量
    chunk = conn.recv(lth)  # 读取用户上传的数据
    data_1 += chunk  # 将本次读取的字节文件，写入上次写入的字节文件尾部
    has_recv_len += len(chunk)  # 将本次读取的文件字节大小，追加到总读取大大小中，计算总读取量
    if has_recv_len == data_length1:  # 当已经读取的大小 == 预知文件总大小
        break  # 接收完毕，结束循环
print(data_1.decode("utf-8"))  # 将已经接收完毕的文件字节转码，打印出来

# 第2条数据
header_2 = conn.recv(4)  # 固定读取4个字节
data_length2 = struct.unpack("i", header_2)[0]  # 预知的总字节大小，减去已接收的字节大小，剩余待接收字节的大小
data_2 = conn.recv(data_length2)  # 读取用户上传的数据
print(data_2.decode("utf-8"))  # 将已经接收完毕的文件字节转码，打印出来

conn.close()  # 关闭与用户的连接
sock.close()  # 关闭服务端
