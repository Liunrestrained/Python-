# 1.应用层：规定数据的格式。
"GET /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n"

# 2.表示层：对应用层数据的编码、压缩（解压缩）、分块、加密（解密）等任务。
"GET /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n你好".encode('utf-8')

# 3.会话层：负责与目标建立、中断连接。
"在发送数据之前，需要会先发送 “连接” 的请求，与远程建立连接后，再发送数据。当然，发送完毕之后，也涉及中断连接的操作。"

# 4.传输层：建立端口到终端的通信，其实就是确定双方的端口信息。
'''数据："GET /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n你好".encode('utf-8')
端口：
	- 目标：80
	- 本地：6784'''

# 5.网络层：标记目标IP信息（IP协议层）。
'''数据："GET /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n你好".encode('utf-8')
端口：
	- 目标：80
	- 本地：6784
IP：
	- 目标IP：110.242.68.3（百度）
	- 本地IP：192.168.10.1'''

# 6.数据链路层：对数据进行分组并设置源和目标的mac地址。
'''数据："POST /s?wd=你好 HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n你好".encode('utf-8')
端口：
	- 目标：80
	- 本地：6784
IP：
	- 目标IP：110.242.68.3（百度）
	- 本地IP：192.168.10.1
MAC：
	- 目标MAC：FF-FF-FF-FF-FF-FF 
	- 本机MAC：11-9d-d8-1a-dd-cd'''

# 7.物理层：将二进制数据再物理媒体上传输。
'''在开发过程中其实只能体现：应用层、表示层、会话层、传输层，其他层的处理都是在网络设备中自动完成的。'''
