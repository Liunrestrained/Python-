import socket

client = socket.socket()
client.connect(("127.0.0.1", 8001))  # 与服务端创建连接

client.sendall(b"hello")  # 简化.encode("utf-8")

reply = client.recv(1024)  # 接收服务端的信息
print(reply)

client.close()
