import os
import uuid
import socket
import select

client_list = []  # socket对象列表

for i in range(5):
    client = socket.socket()  # 实例化socket对象，创建客户端
    client.setblocking(False)  # 无阻塞

    try:
        client.connect(("47.98.134.86", 80))  # 向服务端发送请求连接（不论是否报错都会发送出去），相当于并发发给服务端5个请求
    except BlockingIOError as e:  # try代码出现错误则捕捉该报错
        pass  # 无操作

    client_list.append(client)  # 将已经连接成功的对象添加到列表中

recv_list = []  # 存放已经连接成功，并且将下载请求发送出去的socket连接
while True:
    r, w, e = select.select(recv_list, client_list, [], 0.1)  # r：获取服务器的信息；w:给服务器发送的连接；e：捕获出现异常的socket。
    for sock in w:  # 连接成功的socket循环向网站发起下载请求
        sock.sendall(b"GET/night-logo.png HTTP/1.1\r\nHost:47.98.134.86\r\n\r\n")  # 下载图片的请求，涉及到http协议
        recv_list.append(sock)  # 将已经连接成功，并且将下载请求发送出去的socket连接添加到新列表
        client_list.remove(sock)  # 将已经连接成功，并且将下载请求发送出去的socket连接从旧列表剔除

    for sock in r:  # 循环已经发送下载请求的socket对象
        data = sock.recv(8196)  # 接收服务器发送的信息
        content = data.split(b'\r\n\r\n')[-1]  # 数据处理
        random_file_name = "{}.png", format(str(uuid.uuid4()))  # 设置文件名与文件类型
        with open(os.path.join("images", random_file_name), mode="wb")as f:  # 创建文件并打开
            f.write(content)  # 将服务器的信息写入
        recv_list.remove(sock)  # 将已经写入文件信息的socket对象从第2个列表剔除。

    if not recv_list and client_list:  # 当两个列表都为空，则所有任务都执行完毕，就结束任务
        break


'''
优点：
    可以伪造并发的现象！
'''