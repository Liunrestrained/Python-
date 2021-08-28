import socket
import struct

client = socket.socket()  # 实例化socket对象，创建客户端
client.connect(("127.0.0.1", 8001))  # 指定服务器IP和端口，发送连接请求

# 第一条发送的数据
data_1 = "目标正在连接".encode("utf-8")  # 数据内容，转码字节格式
header_1 = struct.pack("i", len(data_1))  # 划分开头、数据

client.sendall(header_1)  # 先传输内容的长度
client.sendall(data_1)  # 再发送内容本身

# 第二条发送的数据
data_2 = "断开".encode("utf-8")
header_2 = struct.pack("i", len(data_2))

client.sendall(header_2)
client.sendall(data_2)
