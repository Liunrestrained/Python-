import re
import os
import json
import socket
from Pan.Pan_C import config  # 本地配置文件
from Pan.Pan_C.utils import tool  # 本地配置文件


class Client(object):

    def __init__(self):
        self.IP = config.IP  # IP
        self.Port = config.Port  # 端口
        self.conn = socket.socket()  # 创建客户端
        self.username = None  # 当前的登陆状态，None=离线

    def run(self):  # 程序入口
        self.conn.connect((self.IP, self.Port))  # 根据地址、端口连接对应的服务器

        welcome = """
        登录：login 用户名 密码
        注册：register 用户名 密码
        查看：ls 目录
        上传：upload 本地目录 网盘目录
        下载：download 本地目录 网盘目录
        """
        print(welcome)  # 提示用户，命令对应的功能

        method_map = {
            "login": self.login,
            "register": self.register,
            "ls": self.ls,
            "upload": self.upload,
            "download": self.download,
        }  # 后台命令对应的功能方法

        while True:  # 启动循环
            hint = "({})>>>".format(self.username or "未登录")  # username存在时，就是用户名，不存在时就是未登录
            text = input(hint).strip()  # 获取登陆状态后面，用户输入的返回数据
            if not text:  # 命令不能为空
                print("输入不能为空，请重新输入")
                continue  # 重新执行

            if text.upper() == "Q":  # 输入Q\q就退出
                print("记得回来哟！")
                tool.send_message(self.conn, "q")  # 给服务端发送一个q，表示要断开连接
                break

            cmd, *args = re.split(r"\s+", text)  # 对输入的内容进行分割，cmd为命令符，args为内容
            method = method_map.get(cmd)  # 根据用户的命令提示符，在 后台命令对应的功能方法 中寻找对应的函数方法
            if not method:  # 如果找不到，那就是不存在，要重来
                print("命令不存在，请重新输入")
                continue
            method(*args)  # 找到了，就用这个方法包裹用户传输的信息，开始执行对应的方法

        self.conn.close()

    def login(self, *args):  # 接收俩参数：1.用户名、2.密码
        """登录"""
        if len(args) != 2:  # 若不是俩参数，客户端直接判错，让用户重新输入。
            print("你输入的格式好像不正确哎！")
            return
        username, password = args  # 将账户名和密码分开赋值
        tool.send_message(self.conn, "login {} {}".format(username, password))  # 将用户名和密码发送给服务端
        reply = tool.receive(self.conn).decode("utf-8")  # 接收服务端返回的信息
        reply_dict = json.loads(reply)  # 反序列化
        if reply_dict["status"]:  # 服务端返回的status=True，那就是登陆成功；否则就直接打印error。
            self.username = username  # 并将init方法中的username切换为当前用户名，表示在线，“未登录”也会切换为用户名
            print(reply_dict["error"])
            return
        print(reply_dict["error"])

    def register(self, *args):  # 两个元素：1.用户名、2.密码
        """注册"""
        if len(args) != 2:  # 如果不是俩元素，那就在客户端直接判错，让他重新输入
            print("你输入的格式好像不正确哎！")
            return
        username, password = args  # 若是俩元素，就给分开来

        tool.send_message(self.conn, "register {} {}".format(username, password))  # 把账户和密码发到服务端去备案注册
        reply = tool.receive(self.conn).decode("utf-8")  # 接收服务端发回来的信息
        reply_dict = json.loads(reply)  # 将信息反序列化
        if reply_dict["status"]:  # 若得到status=True，那就是注册成功啦，否则就不打印注册成功，直接打印服务端返回的error
            print(reply_dict["error"])  # 然后打印返回信息
            return
        print(reply_dict["error"])  # 然后打印返回信息

    def ls(self, *args):
        """查看目录"""
        if not self.username:  # 如果username=None,那就是还没执行登录或者登陆失败
            print("登陆后才允许查看")
            return
        if not args:  # 没有传入参数，
            cmd = "ls"
        elif len(args) == 1:
            cmd = "ls {}".format(*args)
        else:
            print("格式错误，请重新输入")
            return

        tool.send_message(self.conn, cmd)
        reply = tool.receive(self.conn).decode("utf-8")
        reply_dict = json.loads(reply)
        if reply_dict["status"]:
            print(reply_dict["data"])
            return
        print(reply_dict["error"])

    def upload(self, *args):  # 俩参数：1.本地要上传的文件名字、2.网盘的文件名字
        if not self.username:  # 没登陆的情况
            print("登录后才能上传哦")
            return
        if len(args) != 2:  # 格式不符合规范，信息不完整
            print("格式错误，请重新输入")
            return
        local_file_path, remote_file_path = args  # 信息拆分：1.本地要上传的文件名字、2.网盘的文件名字
        if not os.path.exists(local_file_path):  # 检查本地文件是否存在
            print("文件{}不存在，请重新输入".format(local_file_path))
            return

        tool.send_message(self.conn, "upload {}".format(remote_file_path))  # 本地文件存在，要上传的文件名字发送给网盘
        reply = tool.receive(self.conn).decode("utf-8")  # 接收服务端返回的信息
        reply_dict = json.loads(reply)  # 反序列化
        if not reply_dict["status"]:  # True  # 取字典内容时用了（）而不是［］，就会报错：TypeError: 'dict' object is not callable
            print(reply_dict["error"])  # 打印返回信息
            return

        print("开始上传")
        tool.send_file(self.conn, local_file_path)  # 把要上传的文件传上去

        print("上传完毕")

    def download(self, *args):  # 俩参数：1.下载到本地的文件名字、2.网盘的文件名字
        """下载"""
        if not self.username:  # username=None，没登陆
            print("这个得登陆后才能下载的")
            return
        if len(args) != 2:  # 格式不对
            print("你输入的格式好像不太对，检查一下吧")
            return

        local_file_path, remote_file_path = args  # 俩参数：1.下载到本地的文件名字、2.网盘的文件名字
        seek = 0  # 默认完整下载
        if not os.path.exists(local_file_path):  # 如果本地文件夹不存在这个文件
            tool.send_message(self.conn, "download {}".format(remote_file_path))  # 那就向服务端发起请求下载网盘的指定文件
            mode = "wb"  # 本地的写入方式：从头写入字节形式
        else:
            choice = input("是否断点续传(Y/N)").strip()  # 如果本地存在同名文件，就询问是否进行断点续传
            if choice.upper() == "Y":  # 要续传
                seek = os.stat(local_file_path).st_size  # 获取本地文件大小
                tool.send_message(self.conn, "download {} {}".format(remote_file_path, seek))  # 将要下载的文件名字和大小发给服务端
                mode = "ab"  # 写入方式，追加写入字节形式
            else:  # 不续传
                tool.send_message(self.conn, "download {}".format(remote_file_path))  # 那就向服务端发起请求下载网盘的指定文件
                mode = "wb"  # 覆盖写入

        reply = tool.receive(self.conn).decode("utf-8")  # 获取服务端的信息
        reply_dict = json.loads(reply)  # 反序列化
        if not reply_dict["status"]:  # 网盘文件不存在
            print(reply_dict["error"])  # 打印返回信息
        else:  # 网盘文件存在
            print("开始下载")
            tool.recv_save_file_with_progress(self.conn, local_file_path, mode, seek=seek)  # 下载写入本地
            print("下载完毕")



