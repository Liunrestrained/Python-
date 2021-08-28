import struct  # 处理粘包


def send_message(conn, content):  # 两个参数：1.用户的连接、2.消息的内容
    """将消息发送给客户端,并将数据去粘包处理，也就是增加头部和字节长度"""
    data = content.encode("utf-8")  # 将消息内容转码,赋值给data
    header = struct.pack("i", len(data))  # 加入头部文件以及数据的字节长度
    conn.sendall(header)  # 先发头部和长度
    conn.sendall(data)  # 再发字节文件本身


def receive_message(conn, chunk_size=1024):  # 两个参数：1.用户的连接、2.每次读取的字节大小
    """将客户端发来的做了粘包处理的消息解析读取"""
    has_read_size = 0  # 记录当前已读的头部字节大小
    bytes_list = []  # 记录当前已读的头部字节文件
    while has_read_size < 4:  # 当前已读的头部字节大小 小于 4的时候~
        chunk = conn.recv(4 - has_read_size)  # 则读取4-当前已读的头部字节大小
        has_read_size += len(chunk)  # 将本次循环读取的头部字节大小，追加到记录中
        bytes_list.append(chunk)  # 同时将本次循环读取的头部字节文件，追加到记录中
    header = b"".join(bytes_list)  # 读取头部的循环结束后，将读取的所有头部字节拼接完整
    data_length = struct.unpack("i", header)[0]  # 此时就获取到了头部文件中包含的，总文件的大小信息。

    data_list = []  # 当前已读的字节文件
    has_read_data_size = 0  # 当前已读的字节文件大小
    while has_read_data_size < data_length:  # 当前已读的字节文件大小 小于 总文件的大小
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)  # 根据读取限制，读取本次循环的文件字节
        data_list.append(chunk)  # 将本次读取的文件字节，追加到记录
        has_read_data_size += len(chunk)  # 将本次读取的文件字节大小，追加到记录
    data = b"".join(data_list)  # 全部读取完毕，将所有字节文件拼接完整

    return data  # 返回本次读取的完整文件


def recv_save_file(conn, save_file_path, chunk_size=1024):  # 三个参数：1.用户的连接、2.用户文件的路径、3.每次读写文件的字节大小
    """接收并保存文件"""
    has_read_size = 0  # 记录当前已读的头部字节大小
    bytes_list = []  # 记录当前已读的头部字节文件
    while has_read_size < 4:  # 当前已读的头部字节大小 小于 4的时候~
        chunk = conn.recv(4 - has_read_size)  # 则读取4-当前已读的头部字节大小
        has_read_size += len(chunk)  # 将本次循环读取的头部字节大小，追加到记录中
        bytes_list.append(chunk)  # 同时将本次循环读取的头部字节文件，追加到记录中
    header = b"".join(bytes_list)  # 读取头部的循环结束后，将读取的所有头部字节拼接完整
    data_length = struct.unpack("i", header)[0]  # 此时就获取到了头部文件中包含的，总文件的大小信息。

    file_object = open(save_file_path, mode="wb")
    has_read_data_size = 0  # 当前已读的文件字节大小
    while has_read_data_size < data_length:  # 已读文件大小 < 总文件字节大小
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)  # 根据读取限制，读取本次循环的文件字节
        file_object.write(chunk)  # 将本次读取的文件字节，写入到文件，起始还在内存中
        file_object.flush()  # 将文件从内存刷进硬盘
        has_read_data_size += len(chunk)  # 将本次读取的文件字节大小，追加到记录
    file_object.close()  # 写入完毕，关闭文件


def send_file_by_seek(conn, file_size, file_path, seek=0):  # 4个参数：连接，应该传的大小，文件名字，起始位置
    """读取并发送文件，支持断点续传，从指定的位置开始"""
    header = struct.pack("i", file_size)  # 文件头部、文件大小
    conn.sendall(header)  # 将文件头部、文件大小发送给客户端

    has_send_size = 0  # 已发送的文件字节大小
    file_object = open(file_path, mode="rb")  # 打开指定文件
    if seek:  # 选择续传
        file_object.seek(seek)  # 将光标移动到续传的字节位置
    while has_send_size < file_size:  # 已发送大小 < 文件总大小
        chunk = file_object.read(2048)  # 每次循环读取的文件
        conn.sendall(chunk)  # 将本次循环读取的文件发送过去
        has_send_size += len(chunk)  # 将已经发送的文件大小记录
    file_object.close()  # 发送完毕，关闭文件
