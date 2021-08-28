import socket
import select  # IO多路复用

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个服务端
server.setblocking(False)  # 非阻塞
server.bind(("127.0.0.1", 8001))
server.listen(5)

inputs = [server, ]  # socket对象的列表[server, 第一个客户端, 第二个客户端, ]

while True:
    # 把socket列表当作第一个对象传进去，inputs。
    # r = []——若没有访客发起连接，则r = []，后面的代码不会执行。
    # r = [server,]——当有第一个客户端向某个socket对象发起连接，那该对象就会发生变化，则获取它。则r = [server,]。
    # r = [server,第一个客户端连接conn]——将与客户端的连接放到inputs里面，也就是r = [server,第一个客户端连接conn]。
    # r = [第一个客户端连接conn,]——当第一个客户端发来信息。！= server, 则执行else，接收消息。
    # r = [server, ]——当第2个客户端发来链接
    # r = [server, 第二个客户端, ]——将第2个客户端连接append到inputs。
    # r = [第一个客户端, 第二个客户端, ]——当两个客户端都发来信息。
    # r = [第二个客户端, ]当第2个客户端请求关闭连接，就会发送一个空数据包。系统就会把这个socket对象从inputs中remove掉。
    r, w, e = select.select(inputs, [], [], 0.05)  # 在当前代码的内部，最多花0.05s的时间检测socket对象的列表是否有人发起连接或者发来数据。

    for sock in r:
        if sock == server:
            conn, addr = sock.accept()  # conn是与客户端的连接
            print("有新的访客连接")
            inputs.append(conn)  # 将与客户端的连接放到inputs里面，也就是r = [server,第一个客户端连接conn]
        else:
            data = sock.recv(1024)
            if data:
                print("收到消息", data)
            else:
                print("关闭连接")
                inputs.remove(sock)
    # 干点其他事！
'''
优点：
    1.没有访客连接，就可以干点其他事；
    2.让服务端支持多个客户端同时连接；
'''
