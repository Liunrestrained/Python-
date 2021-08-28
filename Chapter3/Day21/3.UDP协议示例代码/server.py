import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建一个服务端，socket.SOCK_DGRAM这个参数与客户端不一样
server.bind(("127.0.0.1", 8002))

while True:
    data, (host, port) = server.recvfrom(1024)  # 阻塞，data指的接收内容，(host\port)分别指代IP和端口
    print(data, host, port)
    server.sendto("好的".encode("utf-8"), (host, port))  # 回信，参数分别为：内容、（接收者的IP、端口）
