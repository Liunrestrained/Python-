# 面试题（补充代码，实现如下功能）

class Context:

    def __enter__(self):
        return self  # self对象中有do_something的方法

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def do_something(self):
        print('内部执行')


with Context() as ctx:  # with 对象，就会自动执行enter的方法，ctx就是enter的返回值
    print('内部执行')
    ctx.do_something()
    # 当with缩进中的代码执行完毕之后，就会自动执行exit的方法，退出。
