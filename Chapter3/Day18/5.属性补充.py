class Foo(object):

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return "{}-{}".format(self._name, self.age)

# 由于属性和实例变量的调用方式相同，所以在编写时需要注意：属性名称 不要 实例变量 重名。
obj = Foo("武沛齐", 123)
print(obj._name)  # 如果真的想要在名称上创建一些关系，可以让实例变量加上一个下划线
print(obj.name)
