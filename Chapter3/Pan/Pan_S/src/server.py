'''1.客户端'''
import socket  # 网络编程

from Pan.Pan_S import config  # 配置文件


class Socket(object):
    def __init__(self):  # 初始化方法
        self.ip = config.IP  # IP
        self.port = config.Port  # 端口

    def run(self, Func):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建服务端
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # IP重复用
        sock.bind((self.ip, self.port))  # IP\端口
        sock.listen(5)  # 排队人数上限

        while True:
            conn, addr = sock.accept()
            print("(❁´◡`❁)管理员你快看！有一位大帅哔想要跟我连接！")
            instance = Func(conn)  # 实例化Function对象
            while True:
                result = instance.Jumping()  # 会带用户反复去执行这个Jumping()方法,获取这个Function对象的方法Jumping()执行之后的返回值return

                if not result:  # 如果返回一个False,就表示要断开连接。
                    break  # 结束循环

            conn.close()  # 断开连接,写在循环外面，先执行conn.close()就会报"[WinError 10038] 在一个非套接字上尝试了一个操作"这个错!
        sock.close()
