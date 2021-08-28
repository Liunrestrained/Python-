class MyException(Exception):  # 自定义异常类，继承Exception
    title = "请求错误"  # 创建类变量


try:
    raise MyException()  # 实例化异常类对象，并报错
except MyException as e:  # 捕获异常
    print("MyException异常被触发了", e.title)  # 打印错误信息，以及类变量信息
except Exception as e:
    print("Exception", e)
