# 三次握手：
'''
client 向 server 发送一个数据包，表示：请求连接；  # 检测服务端能收消息
server 向 client 发送一个数据包，表示：可以连接；  # 检测服务端能发消息
client 向 server 发起连接。  # 连接
'''

# 四次挥手
'''
client 向 server 发送数据包，表示：请求断开连接；
server 向 client 发送数据包，表示：可以断开连接，但是要等一下；
server 向 client 发送数据包，表示：准备就绪，可以断开连接；
client 向 server 发送数据包，表示：好的
'''
