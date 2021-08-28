import os  # 路径模块
import json  # 数据交换格式
import socket  # 网络编程
import struct  # 解决粘包


def send_data(conn, content):
    data = content.encode('utf-8')  # 文本信息转字节格式
    header = struct.pack('i', len(data))  # 文本头部和内容的大小
    conn.sendall(header)  # 先发大小
    conn.sendall(data)  # 再发文件


def send_file(conn, file_path):
    file_size = os.stat(file_path).st_size  # 获取文件大小
    header = struct.pack('i', file_size)  # 文本头部和内容的大小
    conn.sendall(header)  # 发送文件大小信息

    has_send_size = 0  # 总发送大小
    file_object = open(file_path, mode='rb')  # 打开文件
    while has_send_size < file_size:  # 已发送大小 < 总大小
        chunk = file_object.read(2048)  # 每次读取2048字节
        conn.sendall(chunk)  # 将读取的字节发送
        has_send_size += len(chunk)  # 将发送的字节大小记录
    file_object.close()  # 发送完毕，停止发送


def run():  # 执行函数
    client = socket.socket()  # 创建客户端
    client.connect(('127.0.0.1', 8001))  # 指向服务器地址

    while True:  # 与服务器循环交流
        """
        请发送消息，格式为：
            - 消息：msg|你好呀
            - 文件：file|xxxx.png
        """
        content = input(">>>")  # msg or file  # 输入消息，包括格式
        if content.upper() == 'Q':  # 退出客户端
            send_data(client, "close")  # 给服务端发一条消息，close
            break  # 结束循环，退出客户端
        input_text_list = content.split('|')  # 消息的类型与内容分割
        if len(input_text_list) != 2:  # 消息格式错误（类型与内容不全）
            print("格式错误，请重新输入")
            continue

        message_type, info = input_text_list  # 将消息类型与内容分开赋值

        # 发消息
        if message_type == 'msg':  # 如果是文本消息类型

            # 发消息类型
            send_data(client, json.dumps({"msg_type": "msg"}))  # 把类型字典序列化，给服务端发过去，服务端就知道后面要接收文本类型

            # 发内容
            send_data(client, info)  # 将连接和内容传递给方法，发送给服务端

        # 发文件
        else:
            file_name = info.rsplit(os.sep, maxsplit=1)[-1]  # 分割出文件内容和格式

            # 发消息类型
            send_data(client, json.dumps({"msg_type": "file", 'file_name': file_name}))  # 把文件类型和文件名字典序列化，发送给服务端

            # 发内容
            send_file(client, info)  # 将连接和内容传递给方法

    client.close()  # 退出客户端


if __name__ == '__main__':
    run()
