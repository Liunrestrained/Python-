class Message:  # 类的名称首字母要大写，在python3之后默认都继承object

    def send_email(self, email):  # 创建的一个方法，每个方法的第一个参数就是self
        data = "给{}发送一个空邮件".format(email)
        print(data)


obj = Message()  # 实例化了一个对象obj，创建了一块区域
obj.send_email("777@qq.com")
