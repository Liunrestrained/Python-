import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    text = input("输入发送的内容").strip()
    if text.upper() == "Q":
        break
    client.sendto(text.encode("utf-8"), ("127.0.0.1", 8002))  # 发送内容，先写文本内容，再写服务端的ip和端口
    data, (host, port) = client.recvfrom(1024)  # 接受内容：内容，（IP\端口）
    print(data.decode("utf-8"))

client.close()
