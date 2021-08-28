"""存放一些处理消息发送、粘包处理、文件处理的功能代码块，使用时直接拿去"""

import os  # 路径
import time  # 时间
import struct  # 粘包


def send_message(conn, content):
    """一个消息发送的功能，顺便处理粘包"""
    data = content.encode("utf-8")  # 消息转码
    header = struct.pack("i", len(data))  # 消息的头部文件和长度
    conn.sendall(header)  # 发长度给服务端
    conn.sendall(data)  # 发原信息给服务端


def receive(conn, chunk_size=1024):
    """一个接收信息或文件的功能，包含解读处理粘包后的文件信息，这里仅仅用来接收字符串信息"""
    has_read_size = 0  # 头部已接收长度
    bytes_list = []  # 头部已接受的内容

    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)  # 本次读取的文件(大小)
        has_read_size += len(chunk)  # 将本次读取的大小数据记录
        bytes_list.append(chunk)  # 将本次读取的内容记录

    header = b"".join(bytes_list)  # 将读取的内容拼接
    data_length = struct.unpack("i", header)[0]  # 根据头部文件，获取文件的总大小

    data_list = []  # 文件已接收的字节
    has_read_data_size = 0  # 文件已接收的大小
    while has_read_data_size < data_length:  # 文件已接收的大小 < 文件总大小
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)
        data_list.append(chunk)
        has_read_data_size += len(chunk)

    data = b"".join(data_list)  # 信息拼接完整
    return data  # 返回信息


def send_file(conn, file_path):
    """这是一个文件发送的功能"""
    file_size = os.stat(file_path).st_size  # 获取文件大小
    header = struct.pack("i", file_size)  # 头部文件
    conn.sendall(header)  # 发送文件大小

    has_send_size = 0  # 已发送文件大小
    file_object = open(file_path, mode="rb")  # 打开文件
    while has_send_size < file_size:  # 已发送大小<总大小
        chunk = file_object.read(2048)  # 每次读取的文件字节
        conn.sendall(chunk)  # 将本次读取的文件发送给服务端
        has_send_size += len(chunk)  # 将本次读取的文件大小记录
    file_object.close()  # 发送完毕，关闭文件


def recv_save_file_with_progress(conn, save_file_path, mode, chunk_size=1024, seek=0):
    """下载文件、整体写入和断点续传写入"""
    has_read_size = 0  # 头部文件已经读取大小
    bytes_list = []  # 头部文件已经读取的内容
    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)
        bytes_list.append(chunk)
        has_read_size += len(chunk)
    header = b"".join(bytes_list)
    data_length = struct.unpack("i", header)[0]  # 要下载的文件总大小

    file_object = open(save_file_path, mode=mode)  # 打开文件，wb、ab任选其一
    file_object.seek(seek)  # 光标移动到指定位置

    has_read_data_size = 0  # 文件下载进度
    while has_read_data_size < data_length:  # 已下载<总大小
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)  # 每次接收的大小
        file_object.write(chunk)  # 将接收的文件写入
        file_object.flush()  # 从内存刷到硬盘
        has_read_data_size += len(chunk)  # 记录进度

        percent = "\r{}%".format(int(has_read_data_size * 100 / data_length))  # 下载的百分比进度,保留两位小数
        print(percent, end="")  # 打印进度，不换行，实现百分比变化
        time.sleep(0.5)

    print("")  # 换行，传输完毕100%
    file_object.close()  # 关闭文件
