'''
class MyException(Exception):  # ，首先定义一个异常类：自定义异常需要继承Exception
    pass
try:
    pass  # 当try触发了这个异常，那么就会在内部创建一个MyException的对象，赋值给下方的e。
except MyException as e:  # 要捕获异常，就是要把MyException这个类放在这里。
    print("MyException异常被触发了", e)  # 此处就可以拿到集成了错误信息的对象。
except Exception as e:
    print("Exception", e)'''


# 异常必须有特定的触发条件，例如：索引不存在、键不存在会触发IndexError和KeyError异常。

# 自己定义的异常要想触发，必须使用raise MyException()类实现。
class MyException(Exception):  # 定义一个异常类，继承Exception。
    pass


try:
    raise MyException()  # 实例化异常类的对象,raise是关键。遇到这一句，try中的程序就会立即报错，后方的代码将不再执行。
except MyException as e:  # 此处就会捕获到这个错误信息。
    print("MyException异常被触发了", e)
except Exception as e:  # 此处就会捕获到这个错误信息。
    print("Exception", e)


