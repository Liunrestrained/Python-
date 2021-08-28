import os  # 路径模块
import time  # 时间模块
import socket  # 网络编程模块

client = socket.socket()  # 实例化socket
client.connect(("127.0.0.1", 8001))  # 指向访问的服务端ip\端口

file_path = input("请输入要上传的文件")  # 此处输入文件地址

file_size = os.stat(file_path).st_size  # 获取文件字节大小
client.sendall(str(file_size).encode("utf-8"))  # 将文件大小转换成字符串格式，发送给服务端
# 文件的大小信息，用以确认服务端文件接收以及整合的完整性
print("准备")
time.sleep(3)
print("开始上传...")

file_object = open(file_path, mode="rb")  # 打开这个将要上传的文件
read_size = 0  # 记录直到上次循环总共发送的文件字节大小
while True:  # 循环读取
    chunk = file_object.read(1024)  # 每次读取1024个字节
    client.sendall(chunk)  # 将上次读取的字节发送至服务端
    read_size += len(chunk)  # 发送一次字节文件，就将文件的大小加到总发送大小上
    if read_size == file_size:  # 总发送字节量等于文件总字节量
        break  # 发送结束，循环终止

client.close()  # 关闭客户端(没有总循环)
