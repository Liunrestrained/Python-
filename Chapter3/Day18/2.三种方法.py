class Foo(object):  # object默认继承，可加可不加
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def f1(self):
        print("绑定方法", self.name)

    @classmethod
    def f2(cls):
        print("类方法", cls)

    @staticmethod
    def f3():
        print("静态方法")


# 实例化一个对象
obj = Foo("烧饼", "28")

# 绑定方法
obj.f1()  # 通过对象obj执行方法
Foo.f1(obj)  # 通过类Foo执行方法

# 类方法
obj.f2()  # 通过对象执行方法
Foo.f2()  # 通过类执行方法

# 静态方法
obj.f3()  # 通过对象执行方法
Foo.f3()  # 通过类执行方法
