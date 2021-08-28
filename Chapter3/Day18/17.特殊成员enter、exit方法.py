class Foo(object):

    def __enter__(self):
        print("进来了")
        return 666

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("出去了")


obj = Foo()
with obj as f:
    print(f)
'''上下文管理的语法，可以用在网络访问后自动关闭连接'''
