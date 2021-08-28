'''少用但重要，eg：单例模式'''


class Foo(object):  # 若不写__new__方法，创建对象时则默认会到继承的object类中去寻找方法
    def __init__(self, name):
        print("第2步，初始化对象，在空对象中创建数据")
        self.name = name

    def __new__(cls, *args, **kwargs):  # 可写可不写，写了就是Foo类的绑定方法，不写就去继承的object中寻找它
        print("第1步，先创建空对象并返回")
        return object.__new__(cls)


obj = Foo("大壮")
