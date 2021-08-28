import os  # 路径模块
import json  # 数据转换
import socket  # 网络编程
import struct  # 解决粘包


def recv_data(conn, chunk_size=1024):  # 读取文本数据方法
    has_read_size = 0  # 截至目前总共读取的字节大小
    bytes_list = []  # 截止至目前总共读取的字节文件
    while has_read_size < 4:  # 当目前已读的字节文件大小 < 4: 等式被打破就会结束循环
        chunk = conn.recv(4 - has_read_size)  # 阻塞，读取字节文件(4减去之前总共读取的字节文件大小==剩余待读取的字节文件大小)
        has_read_size += len(chunk)  # 把上级代码已经读取的字节文件大小，记录到总共已读的文件大小中
        bytes_list.append(chunk)  # 将已经读取的字节文件添加到，已经读取过的字节文件列表中
    header = b"".join(bytes_list)  # 循环结束后，将已经读取的字节文件列表，拼接起来
    data_length = struct.unpack('i', header)[0]  # 读取头部文件，获取文件的总大小

    data_list = []  # 暂时存储已读字节文件
    has_read_data_size = 0  # 已读字节文件大小
    while has_read_data_size < data_length:  # 已读文件大小 < 文件总大小
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size  # 单次读取字节大小： 若剩余文件大小>1024,就用1024；否则就用剩余文件大小读取
        chunk = conn.recv(size)  # 读取本次循环的字节文件
        data_list.append(chunk)  # 将本次循环读取的字节文件添加到列表，储存
        has_read_data_size += len(chunk)  # 将本次读取的文件字节大小追加到已读大小

    data = b"".join(data_list)  # 将已读字节文件拼接

    return data  # 返回已读的总文件


def recv_file(conn, save_file_name, chunk_size=1024):  # 读取文件数据方法
    save_file_path = os.path.join('file', save_file_name)  # 信息类型区分与文件路径拼接
    has_read_size = 0  # 已读文件字节大小
    bytes_list = []  # 已读字节文件内容
    while has_read_size < 4:  # 已读文件大小 < 4
        chunk = conn.recv(4 - has_read_size)  # 阻塞，读取字节文件(4减去之前总共读取的字节文件大小==剩余待读取的字节文件大小)
        has_read_size += len(chunk)  # 把上级代码已经读取的字节文件大小，记录到总共已读的文件大小中
        bytes_list.append(chunk)  # 将已经读取的字节文件添加到，已经读取过的字节文件列表中
    header = b"".join(bytes_list)  # 循环结束后，将已经读取的字节文件列表，拼接起来
    data_length = struct.unpack('i', header)[0]  # 读取头部文件，获取文件的总大小

    file_object = open(save_file_path, mode="wb")  # 打开文件
    has_read_data_size = 0  # 当前已写入文件大小
    while has_read_data_size < data_length:  # 当前已写入文件大小 < 文件的总大小
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size  # 单次读取字节大小： 若剩余文件大小>1024,就用1024；否则就用剩余文件大小读取
        chunk = conn.recv(size)  # 读取当前循环的字节
        file_object.write(chunk)  # 将本次读取的字节写入文件(内存中)
        file_object.flush()  # 将本次写入内存的文件直接刷进文件
        has_read_data_size += len(chunk)  # 将本次循环读取的字节大小追加到已写文件大小中
    file_object.close()  # 写入完毕，关闭文件


def run():  # 执行文件
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建服务端
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # IP重复使用的功能
    sock.bind(('127.0.0.1', 8001))  # 检测本机IP、端口
    sock.listen(5)  # 容纳排队人数

    while True:  # 循环接客
        conn, addr = sock.accept()  # 当前访客的IP、mac

        while True:  # 循环执行信息传递
            message_type = recv_data(conn).decode('utf-8')  # 获取用户发送的消息
            if message_type == 'close':  # 关闭连接
                print("关闭与服务器连接")
                break
            # 文件：{'msg_type':'file', 'file_name':"xxxx.xx" }
            # 消息：{'msg_type':'msg'}
            message_type_info = json.loads(message_type)  # 反序列化消息
            if message_type_info['msg_type'] == 'msg':  # 如果是文本类型消息
                data = recv_data(conn)  # 那就执行该文本方法
                print("接收到消息", data.decode("utf-8"))  # 接收函数执行的返回值
            else:  # 否则就执行文件类型方法
                file_name = message_type_info['file_name']  # 文件路径
                print("接收到文件，要保存到：", file_name)  # 打印文件路径
                recv_file(conn, file_name)  # 执行文件类型方法
        conn.close()  # 执行完毕，关闭连接
    sock.close()  # 关闭服务器


if __name__ == '__main__':
    run()
