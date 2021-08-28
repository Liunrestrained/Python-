class MyException(Exception):
    def __init__(self, msg, *args, **kwargs):  # 自定义一个初始化方法，并附参数
        super().__init__(*args, **kwargs)  # 执行父类中的初始化方法，并将参数传递
        self.msg = msg  # 定义一个实例变量


try:
    raise MyException("xxx失败了")  # 实例化异常类的对象，并将变量传递给msg
except MyException as e:  # 捕获到错误信息
    print("MyException异常被触发了", e.msg)  # 报错，并打印实例变量的内容
except Exception as e:  # 模糊处理
    print("Exception", e)
