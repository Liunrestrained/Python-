import socket

client = socket.socket()  # 1.实例化socket对象
client.connect(("127.0.0.1", 8001))  # 2.向指定的服务端发起连接请求（阻塞）10s

client.sendall("hello".encode("utf-8"))  # 3.连接成功后发送消息

reply = client.recv(1024)  # 4.阻塞，等待客户端回复消息；每次最多接收1024字节
print(reply)

client.close()  # 5.关闭连接
