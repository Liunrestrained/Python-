class Message:

    def __init__(self, content):  # 初始化方法
        self.data = content

    def send_email(self, email):
        data = "给{}发一条信息{}".format(email, self.data)
        print(data)

    def send_wechat(self, vid):
        data = "给我的朋友{}发一条简讯{}".format(vid, self.data)
        print(data)


# 对象 = 类名()  # 自动执行类中的__init__方法。

# 1.根据类创建一个对象，在内存中创建一块区域
# 2.执行__init__方法，模块会将创建的那块区域的内存地址当作self参数传递进去。

msg = Message("注册成功")

msg.send_email("77889@qq.com")
msg.send_wechat("大笨猪")
