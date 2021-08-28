'''-------------------------server端---------------------------------------'''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8001))
sock.listen(5)
sock.setblocking(False)  # 加上后，后面的代码就都变成了非阻塞

conn, addr = sock.accept()  # 非阻塞；阻塞的状态下，程序会卡在这里，什么都不能做，很浪费资源。

client_data = conn.recv(1024)  # 非阻塞
print(client_data.decode('utf-8'))

conn.close()
sock.close()

'''-------------------------client端---------------------------------------'''
import socket

client = socket.socket()
client.setblocking(False)  # 加上就是非阻塞

# 非阻塞
client.connect(("127.0.0.1", 8001))
client.sendall("你爱我我爱你".encode("utf-8"))
client.close()

'''非阻塞的程序在运行时，一旦遇到accept、recv、connect就会抛出BlockingIOError的异常。
这并不是代码出现错误，'而是原来的IO阻塞变成非阻塞之后，由于没有收到相关的IO请求而抛出的固定错误。
非阻塞的代码一般与IO多路复用搭配使用，从而产生更大的作用'''