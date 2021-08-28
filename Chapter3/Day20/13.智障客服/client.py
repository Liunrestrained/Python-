import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket对象
client.connect(("127.0.0.1", 8001))  # 输入对应的服务器IP和端口

message = client.recv(1024)  # 接收服务器的系统登陆信息
print(message.decode("utf-8"))  # 打印信息，转换编码

while True:  # 开始循环提问
    content = input("请输入(Q退出)")
    if content.upper() == "Q":  # 键入Q退出
        break
    client.sendall(content.encode("utf-8"))  # 将提出的请求转换编码，发送给服务端

    reply = client.recv(1024)  # 接收服务端的回信
    print(reply.decode("utf-8"))  # 转换编码，并打印

client.close()  # 关闭客户端
