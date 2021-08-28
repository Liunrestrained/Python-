class Foo(object):
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return "{}-{}".format(self.name, other.name)


v1 = Foo("俞伯牙")
v2 = Foo("钟子期")
# 对象+值，内部会去执行__add__方法，并将+后面的值当作参数传递过去。
v3 = v1 + v2
print(v3)
