class Foo:

    def __init__(self, name):
        self.name = name

    def f1(self):
        print(123)
        return 123

    @property  # 绑定方法 + 特殊装饰器 组合创造出来的，在调用方法时可以不加括号
    def f2(self):
        print(456)
        return 456


obj = Foo("杨卫宁")

obj.f1()

obj.f2
